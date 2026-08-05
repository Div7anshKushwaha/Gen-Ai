from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r"C:\Users\divya\Projects\Feature_Engineering\Notes",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(f"Total Documents: {len(docs)}")

print(docs[0].metadata)
print(docs[0].page_content[:500])


"""
Pattern              Meaning
-----------------------------------------------------
*.pdf                All PDFs in current folder
**/*.pdf             All PDFs in all subfolders
*.txt                All text files
*.csv                All CSV files
*.docx               All Word files
*.md                 All Markdown files
*                    Every file
**/*                 Every file recursively
A*.pdf               PDFs starting with A
*Notes.pdf           PDFs ending with "Notes"
*Feature*.pdf        PDFs containing "Feature"
?.pdf                Single-character filename
[1-5]*.pdf           Files starting with 1-5
[A-C]*.pdf           Files starting with A, B or C
"""

"""
Difference between load() and lazy_load()
load()	                                                lazy_load()
Returns a list	                                        Returns a generator
Loads all documents into memory at once	                Loads one document at a time
Supports len(docs)	                                    ❌ No len()
Supports docs[0]	                                    ❌ No indexing
Easier for beginners	                                Better for very large datasets
"""