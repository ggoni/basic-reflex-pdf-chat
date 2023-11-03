from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA


def dumb_answer(question: str) -> str:
    return "¿Me podría repetir la pregunta"


def qa_machine(query: str, vector_store: FAISS):

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=vector_store.as_retriever())
    return qa({"query": query})['result']
