from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

load_dotenv()

# ---------------- Documents ---------------- #

docs = [

    Document(
        page_content="""
The Grand Canyon is one of the most visited natural wonders in the world.
Photosynthesis is the process by which green plants convert sunlight into energy.
Millions of tourists travel to see it every year.
The rocks date back millions of years.
""",
        metadata={"source": "Doc1"},
    ),

    Document(
        page_content="""
In medieval Europe, castles were built primarily for defense.
The chlorophyll in plant cells captures sunlight during photosynthesis.
Knights wore armor made of metal.
Siege weapons were often used to breach castle walls.
""",
        metadata={"source": "Doc2"},
    ),

    Document(
        page_content="""
Basketball was invented by Dr. James Naismith.
It was originally played using peach baskets.
The NBA is now one of the biggest sports leagues in the world.
""",
        metadata={"source": "Doc3"},
    ),

    Document(
        page_content="""
The history of cinema began in the late 1800s.
Thomas Edison contributed to early motion pictures.
Photosynthesis does not occur in animal cells.
Modern filmmaking uses CGI and advanced sound design.
""",
        metadata={"source": "Doc4"},
    ),

]

# ---------------- Embedding Model ---------------- #

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- Vector Store ---------------- #

vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# ---------------- Base Retriever ---------------- #

base_retriever = vector_store.as_retriever(
    search_kwargs={"k": 4}
)

# ---------------- LLM ---------------- #

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ---------------- Compressor ---------------- #

compressor = LLMChainExtractor.from_llm(llm)

# ---------------- Contextual Compression Retriever ---------------- #

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# ---------------- Query ---------------- #

query = "What is photosynthesis?"

results = compression_retriever.invoke(query)

print("=" * 80)
print("CONTEXTUAL COMPRESSION RETRIEVER")
print("=" * 80)

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 80)
    print(doc.page_content)


"""                           USER QUERY
                  "What is photosynthesis?"
                               │
                               ▼
                ContextualCompressionRetriever
                               │
         ┌─────────────────────┴─────────────────────┐
         │                                           │
         ▼                                           ▼
  Base Retriever                             LLM Compressor
 (FAISS / Chroma)                      (LLMChainExtractor + LLM)
         │
         ▼
 Convert query to embedding
         │
         ▼
 Search Vector Store
         │
         ▼
 Retrieve Top-k Documents
         │
         ▼
 ┌─────────────────────────────────────────────────────┐
 │ Doc 1                                               │
 │ The Grand Canyon is famous...                       │
 │ Photosynthesis converts sunlight into energy...     │
 │ Millions of tourists visit every year...            │
 └─────────────────────────────────────────────────────┘

 ┌─────────────────────────────────────────────────────┐
 │ Doc 2                                               │
 │ Castles were built for defense...                   │
 │ Chlorophyll captures sunlight...                    │
 │ Knights wore armor...                               │
 └─────────────────────────────────────────────────────┘

 ┌─────────────────────────────────────────────────────┐
 │ Doc 3                                               │
 │ Basketball was invented by James Naismith...        │
 └─────────────────────────────────────────────────────┘
                               │
                               ▼
                 Send every document to the LLM
                               │
                               ▼
         LLM extracts only the parts useful for
                answering the user's question
                               │
                               ▼
 ┌─────────────────────────────────────────────────────┐
 │ Doc 1                                               │
 │ ✔ Photosynthesis converts sunlight into energy.     │
 └─────────────────────────────────────────────────────┘

 ┌─────────────────────────────────────────────────────┐
 │ Doc 2                                               │
 │ ✔ Chlorophyll captures sunlight.                    │
 └─────────────────────────────────────────────────────┘

 ┌─────────────────────────────────────────────────────┐
 │ Doc 3                                               │
 │ ✘ Removed (not related)                             │
 └─────────────────────────────────────────────────────┘
                               │
                               ▼
                  Compressed Documents
                               │
                               ▼
                     Returned to your RAG
                               │
                               ▼
                     Sent to the Final LLM
                               │
                               ▼
                     Final Answer Generated"""