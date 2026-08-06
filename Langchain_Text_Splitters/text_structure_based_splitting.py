from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0
)

# Perform the split
chunks = splitter.split_text(text)

print("Total Chunks:", len(chunks))
print()

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}")
    print(chunk)
    print("-" * 60)



"""
                   Entire Text
                        │
                        ▼
            Try "\n\n" (Paragraph)
                        │
          ┌─────────────┴─────────────┐
          │                           │
      Fits in size?              Too Large
          │                           │
          ▼                           ▼
     Create Chunk              Try "\n"
                                      │
                           ┌──────────┴──────────┐
                           │                     │
                       Fits?                Too Large
                           │                     │
                           ▼                     ▼
                    Create Chunk           Try Space (" ")
                                                 │
                                      ┌──────────┴──────────┐
                                      │                     │
                                  Fits?                Too Large
                                      │                     │
                                      ▼                     ▼
                               Create Chunk          Split Characters
"""    