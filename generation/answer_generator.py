import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage


def generate_answer(chunks, query):

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0
    )

    prompt = f"Answer this question: {query}\n\n"

    for chunk in chunks:

        data = json.loads(chunk.metadata["original_content"])

        prompt += data.get("raw_text", "") + "\n\n"

    message = HumanMessage(content=[{"type": "text", "text": prompt}])

    response = llm.invoke([message])

    return response.content