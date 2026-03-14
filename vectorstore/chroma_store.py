from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL, VECTOR_DB_PATH


def create_vector_store(documents):

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    db = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH,
        collection_metadata={"hnsw:space": "cosine"}
    )

    return db