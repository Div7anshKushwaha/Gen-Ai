from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("ML.pdf")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)

print(docs[1].metadata)


"""
# Loader                               OCR      Speed       Best For
# -----------------------------------------------------------------------------
# PyPDFLoader                          ❌       ⭐⭐⭐        General PDFs
# PyMuPDFLoader                        ❌       ⭐⭐⭐⭐⭐      Large PDFs & Books
# PDFPlumberLoader                     ❌       ⭐⭐⭐        Tables & Financial PDFs
# UnstructuredPDFLoader                Optional ⭐⭐         Complex Layouts
# AmazonTextractPDFLoader              ✅       ⭐⭐⭐        Scanned PDFs
# MathpixPDFLoader                     ✅       ⭐⭐⭐        Scientific Papers
# AzureAIDocumentIntelligenceLoader    ✅       ⭐⭐⭐        Enterprise OCR
"""