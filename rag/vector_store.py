from pathlib import Path

from langchain_community.vectorstores import FAISS
from .embeddings import get_embeddings

VECTORSTORE_PATH='vectorstore'

def create_vector_store(chunks):
    embeddings=get_embeddings()

    vector_store=FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    Path(VECTORSTORE_PATH).mkdir(
        exist_ok=True
    )
    vector_store.save_local(VECTORSTORE_PATH)
    return vector_store

def load_vector_store():
    embeddings=get_embeddings()
    vector_store=FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store