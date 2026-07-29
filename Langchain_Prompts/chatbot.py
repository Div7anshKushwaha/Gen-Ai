from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",temperature=0.1
)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    print("print exit to exit")
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)




