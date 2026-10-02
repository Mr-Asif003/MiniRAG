import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


MODEL_NAME = os.getenv(
    "HF_MODEL",
    "Qwen/Qwen3.8-27B"
)

PROVIDER = os.getenv(
    "HF_PROVIDER",
    "auto"
)


def get_client() -> InferenceClient:
    """
    Create and return the Hugging Face inference client.
    """

    api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not api_key:
        raise ValueError(
            "HF_TOKEN is not configured in .env"
        )

    return InferenceClient(
        api_key=api_key,
        provider=PROVIDER
    )


def generate_answer(context: str, question: str) -> str:
    """
    Generate a RAG answer using Hugging Face Inference Providers.
    """

    client = get_client()

    system_prompt = """
You are a helpful RAG assistant.

Your job is to answer the user's question using ONLY
the information provided in the context.

Rules:

1. Do not make up information.
2. Do not use outside knowledge.
3. If the answer cannot be found in the context, say:

"I don't have enough information in the provided data."

4. Keep the answer concise and clear.
5. Use a friendly and conversational tone.
6. You may provide practical suggestions only when they
   are directly supported by the provided context.
7. Clearly distinguish facts from suggestions.
"""

    user_prompt = f"""
Context:
----------------
{context}
----------------

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.2,
        max_tokens=512,
    )

    return response.choices[0].message.content