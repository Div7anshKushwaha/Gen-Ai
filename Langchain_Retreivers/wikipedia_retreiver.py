from langchain_community.retrievers import WikipediaRetriever

# Create the retriever
retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

# Retrieve documents
docs = retriever.invoke("Virat Kohli")

print(f"Total Documents Retrieved: {len(docs)}\n")

for i, doc in enumerate(docs, start=1):
    print(f"Document {i}")
    print("-" * 80)
    print(doc.page_content)
    print()
    print(doc.metadata)
    print("=" * 80)