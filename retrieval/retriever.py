def get_relevant_chunks(db, query):

    retriever = db.as_retriever(search_kwargs={"k": 3})

    return retriever.invoke(query)