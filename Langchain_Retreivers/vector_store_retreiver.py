from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ---------------- Embedding Model ---------------- #

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- Documents ---------------- #

documents = [

    Document(
        page_content="LangChain helps developers build LLM applications easily."
    ),

    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),

    Document(
        page_content="Embeddings convert text into high-dimensional vectors."
    ),

    Document(
        page_content="Hugging Face provides many free embedding models."
    ),
]

# ---------------- Create Vector Store ---------------- #

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# ---------------- Convert to Retriever ---------------- #

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

# ---------------- Query ---------------- #

query = "What is Chroma used for?"

results = retriever.invoke(query)

print("=" * 80)
print("USING RETRIEVER")
print("=" * 80)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print(doc.page_content)

# ---------------- Similarity Search ---------------- #

results = vector_store.similarity_search(
    query=query,
    k=2
)

print("\n")
print("=" * 80)
print("USING VECTOR STORE")
print("=" * 80)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print(doc.page_content)