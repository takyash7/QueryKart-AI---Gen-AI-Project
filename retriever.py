from langchain_community.vectorstores import FAISS

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

# ==========================================
# EMBEDDING MODEL
# ==========================================

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================
# LOAD VECTOR DATABASE
# ==========================================

vector_store = FAISS.load_local(

    "faiss_index",

    embedding_model,

    allow_dangerous_deserialization=True
)

# ==========================================
# CREATE RETRIEVER
# ==========================================

retriever = vector_store.as_retriever(

    search_kwargs={"k": 4}
)