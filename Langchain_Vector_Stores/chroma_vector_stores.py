from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ---------------- Embedding Model ---------------- #

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- Vector Store ---------------- #

vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="my_chroma_db"
)

# ---------------- Documents ---------------- #

docs = [

    Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"},
    ),

    Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"},
    ),

    Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"},
    ),

    Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"},
    ),

    Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"},
    ),
]

# ---------------- Add Documents ---------------- #

vector_store.add_documents(docs)

print("\nDocuments Added Successfully\n")

# ---------------- View Documents ---------------- #

data = vector_store.get(
    include=["documents", "metadatas"]
)

print("=" * 80)
print("ALL DOCUMENTS")
print("=" * 80)

for i, (doc, metadata) in enumerate(zip(data["documents"], data["metadatas"]), start=1):
    print(f"\nDocument {i}")
    print(doc)
    print(metadata)

# ---------------- Similarity Search ---------------- #

print("\n")
print("=" * 80)
print("SIMILARITY SEARCH")
print("=" * 80)

results = vector_store.similarity_search(
    query="Who among these are bowlers?",
    k=2
)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 80)

# ---------------- Similarity Search With Score ---------------- #

print("\n")
print("=" * 80)
print("SIMILARITY SEARCH WITH SCORE")
print("=" * 80)

results = vector_store.similarity_search_with_score(
    query="Who among these are bowlers?",
    k=2
)

for doc, score in results:
    print(f"Score : {score}")
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 80)

# ---------------- Metadata Filtering ---------------- #

print("\n")
print("=" * 80)
print("METADATA FILTERING")
print("=" * 80)

results = vector_store.similarity_search(
    query="",
    filter={"team": "Chennai Super Kings"}
)

for doc in results:
    print(doc.page_content)
    print(doc.metadata)
    print("-" * 80)

# ---------------- Get Document IDs ---------------- #

data = vector_store.get()

print("\n")
print("=" * 80)
print("DOCUMENT IDS")
print("=" * 80)

for i, doc_id in enumerate(data["ids"], start=1):
    print(f"Document {i} ID : {doc_id}")

# ---------------- Update Document ---------------- #

updated_doc = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"},
)

# Assuming the first document is Virat Kohli
virat_doc_id = data["ids"][0]

vector_store.update_document(
    document_id=virat_doc_id,
    document=updated_doc
)

print("\nVirat Kohli document updated successfully.")

# ---------------- View Updated Documents ---------------- #

updated_data = vector_store.get(
    include=["documents", "metadatas"]
)

print("\n")
print("=" * 80)
print("UPDATED DOCUMENTS")
print("=" * 80)

for doc, metadata in zip(updated_data["documents"], updated_data["metadatas"]):
    print(doc)
    print(metadata)
    print("-" * 80)

# ---------------- Delete Document ---------------- #

vector_store.delete(
    ids=[virat_doc_id]
)

print("\nVirat Kohli document deleted successfully.")

# ---------------- View Remaining Documents ---------------- #

remaining_data = vector_store.get(
    include=["documents", "metadatas"]
)

print("\n")
print("=" * 80)
print("REMAINING DOCUMENTS")
print("=" * 80)

for doc, metadata in zip(remaining_data["documents"], remaining_data["metadatas"]):
    print(doc)
    print(metadata)
    print("-" * 80)