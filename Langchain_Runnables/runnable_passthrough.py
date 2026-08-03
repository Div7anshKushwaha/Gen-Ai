from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

# ---------------- Model ---------------- #

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ---------------- Parser ---------------- #

parser = StrOutputParser()

# ---------------- Prompt 1 ---------------- #

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# ---------------- Prompt 2 ---------------- #

prompt2 = PromptTemplate(
    template="Explain the following joke:\n\n{text}",
    input_variables=["text"]
)

# ---------------- Joke Generation Chain ---------------- #

joke_gen_chain = RunnableSequence(
    first=prompt1,
    middle=[model],
    last=parser
)

# ---------------- Parallel Chain ---------------- #

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(
            first=prompt2,
            middle=[model],
            last=parser
        ),
    }
)

# ---------------- Final Chain ---------------- #

final_chain = RunnableSequence(
    first=joke_gen_chain,
    middle=[],
    last=parallel_chain
)

# ---------------- Invoke ---------------- #

result = final_chain.invoke({"topic": "cricket"})

print(result)

print()
final_chain.get_graph().print_ascii()