from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

prompt = PromptTemplate(
    template="Write a summary for the following text:\n\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke(
    {"text": docs[0].page_content}
)

print(result)