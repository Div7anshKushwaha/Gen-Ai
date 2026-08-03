from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

# Model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Parser
parser = StrOutputParser()

# Prompts
prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}",
    input_variables=["topic"]
)

# Tweet Chain
tweet_chain = RunnableSequence(
    first=prompt1,
    middle=[model],
    last=parser
)

# LinkedIn Chain
linkedin_chain = RunnableSequence(
    first=prompt2,
    middle=[model],
    last=parser
)

# Parallel Chain
parallel_chain = RunnableParallel(
    {
        "tweet": tweet_chain,
        "linkedin": linkedin_chain
    }
)

# Invoke
result = parallel_chain.invoke({"topic": "AI"})

print("Tweet:\n")
print(result["tweet"])

print("\n" + "=" * 70 + "\n")

print("LinkedIn Post:\n")
print(result["linkedin"])

print("\n")
parallel_chain.get_graph().print_ascii()