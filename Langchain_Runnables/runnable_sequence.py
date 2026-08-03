from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

# Load Model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Output Parser
parser = StrOutputParser()

# First Prompt
prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# Second Prompt
prompt2 = PromptTemplate(
    template="Explain the following joke:\n\n{text}",
    input_variables=["text"]
)

# Runnable Sequence
chain = RunnableSequence(
    first=prompt1,
    middle=[model, parser, prompt2, model],
    last=parser
)

# Invoke
result = chain.invoke({"topic": "AI"})

print(result)

# Visualize the chain
print()
chain.get_graph().print_ascii()