from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")

text = "Hello how are you ?"
document = ["my name is divyansh","I am doing BS in Data Science","From IIT Madras"]
vectors = embeddings.embed_query(text)
vector = embeddings.embed_documents(document)
print(vectors)
print(vector)