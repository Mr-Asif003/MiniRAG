from .vector_store import load_vector_store

def retrieve_documents(query,k=3):
    vector_store=load_vector_store()
    documennts=vector_store.similarity_search(
        query=query,
        k=k
    )
    return documennts