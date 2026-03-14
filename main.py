from config import PDF_PATH

from ingestion.partition import partition_document
from ingestion.chunking import create_chunks
from ingestion.summariser import summarise_chunks

from vectorstore.chroma_store import create_vector_store
from retrieval.retriever import get_relevant_chunks
from generation.answer_generator import generate_answer


def run_pipeline():

    elements = partition_document(PDF_PATH)

    chunks = create_chunks(elements)

    docs = summarise_chunks(chunks)

    db = create_vector_store(docs)

    query = "How many attention heads does the transformer use?"

    retrieved = get_relevant_chunks(db, query)

    answer = generate_answer(retrieved, query)

    print("\nFINAL ANSWER:\n")
    print(answer)


if __name__ == "__main__":

    run_pipeline()