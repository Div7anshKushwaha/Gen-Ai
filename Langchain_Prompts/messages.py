from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",temperature=0.1
)


messages = [SystemMessage(content = "you are a helpful assisstant"),
HumanMessage(content="tell me about Langchain")]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))








