import streamlit as st

from rag.data_manager import save_user
from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vector_store import create_vector_store
from rag.rag_pipeline import ask_rag


st.set_page_config(
    page_title="MiniRAG",
    page_icon="🤖"
)


st.title("🤖 MiniRAG")

st.write(
    "A simple Retrieval-Augmented Generation application "
    "using LangChain, Hugging Face and FAISS."
)


# --------------------------------------------------
# USER DATA
# --------------------------------------------------

st.header("1. Add User Data")

name = st.text_input("Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=20
)

city = st.text_input("City")

skills = st.text_input(
    "Skills",
    placeholder="Java, Python, React"
)

education = st.text_input(
    "Education",
    placeholder="B.Tech Computer Science"
)

interests = st.text_input(
    "Interests",
    placeholder="AI, System Design"
)


if st.button("Upload User Data"):

    if not name:
        st.error("Please enter a name.")

    else:

        user = {
            "name": name,
            "age": age,
            "city": city,
            "skills": [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ],
            "education": education,
            "interests": [
                interest.strip()
                for interest in interests.split(",")
                if interest.strip()
            ]
        }

        save_user(user)

        # Load JSON
        documents = load_documents()

        # Create chunks
        chunks = split_documents(documents)

        # Create vector store
        create_vector_store(chunks)

        st.success(
            "User data uploaded and vector store created!"
        )


# --------------------------------------------------
# QUERY
# --------------------------------------------------

st.divider()

st.header("2. Query User Data")

query = st.text_input(
    "Enter your question",
    placeholder="What skills does Asif have?"
)


if st.button("Query Data"):

    if not query:
        st.warning("Please enter a question.")

    else:

        try:

            answer, documents = ask_rag(query)

            st.subheader("Answer")

            st.write(answer)

            with st.expander("Retrieved Context"):

                for document in documents:

                    st.write(
                        document.page_content
                    )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )