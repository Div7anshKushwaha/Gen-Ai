from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# LLM
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Prompt
prompt = PromptTemplate(
    template="""
Answer the following question from the given text.

Question:
{question}

Text:
{text}
""",
    input_variables=["question", "text"]
)

# Output Parser
parser = StrOutputParser()

# URL
url ='https://www.ibm.com/think/topics/machine-learning'

# Load webpage
loader = WebBaseLoader(url)
docs = loader.load()

# LCEL Chain
chain = prompt | model | parser

# Invoke
result = chain.invoke({
    "question": "What is the topic that we are talking about?",
    "text": docs[0].page_content
})

print(result)