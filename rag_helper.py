from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import FAISS

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_core.documents import Document

# ==========================================
# LOAD SCHEMA FILE
# ==========================================

with open(
    "schema_context.txt",
    "r",
    encoding="utf-8"
) as file:

    schema_text = file.read()

# ==========================================
# CHUNKING
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)

chunks = text_splitter.split_text(
    schema_text
)

# ==========================================
# CONVERT TO DOCUMENTS
# ==========================================

documents = [

    Document(page_content=chunk)

    for chunk in chunks
]

# ==========================================
# EMBEDDING MODEL
# ==========================================

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================
# CREATE VECTOR DATABASE
# ==========================================

vector_store = FAISS.from_documents(

    documents,

    embedding_model
)

# ==========================================
# SAVE VECTOR DATABASE
# ==========================================

vector_store.save_local(
    "faiss_index"
)

print("✅ FAISS vector database created successfully.")