from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)

load_dotenv()


# Function to count words
def word_count(text):
    return len(text.split())


# Model
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Parser
parser = StrOutputParser()

# Prompt
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# Joke Generation Chain
joke_gen_chain = RunnableSequence(
    first=prompt,
    middle=[model],
    last=parser
)

# Parallel Chain
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(word_count)
    }
)

# Final Chain
final_chain = RunnableSequence(
    first=joke_gen_chain,
    middle=[],
    last=parallel_chain
)

# Invoke
result = final_chain.invoke({"topic": "AI"})

final_result = f"""
{result['joke']}

Word Count: {result['word_count']}
"""

print(final_result)

print()
final_chain.get_graph().print_ascii()