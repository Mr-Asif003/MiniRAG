from .retriever import retrieve_documents
from .generator import generate_answer

def ask_rag(question):
    documents=retrieve_documents(
        question,
        k=3
    )

    context="\n\n".join(
        document.page_content 
        for document in documents
    )
    answer=generate_answer(
        context=context,
        question=question
    )
    return answer,documents