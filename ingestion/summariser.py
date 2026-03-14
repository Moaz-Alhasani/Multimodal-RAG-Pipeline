import json
from typing import List

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.documents import Document

from .content_parser import separate_content_types


def create_ai_summary(text: str, tables: List[str], images: List[str]):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0
    )

    prompt = f"""
You are creating a searchable description.

TEXT:
{text}
"""

    message_content = [{"type": "text", "text": prompt}]

    for img in images:

        message_content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": img,
            }
        })

    message = HumanMessage(content=message_content)

    response = llm.invoke([message])

    return response.content


def summarise_chunks(chunks):

    documents = []

    for chunk in chunks:

        content = separate_content_types(chunk)

        if content["tables"] or content["images"]:

            enhanced = create_ai_summary(
                content["text"],
                content["tables"],
                content["images"]
            )

        else:
            enhanced = content["text"]

        doc = Document(
            page_content=enhanced,
            metadata={
                "original_content": json.dumps({
                    "raw_text": content["text"],
                    "tables_html": content["tables"],
                    "images_base64": content["images"]
                })
            }
        )

        documents.append(doc)

    return documents