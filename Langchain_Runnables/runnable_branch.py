from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text:\n\n{text}",
    input_variables=["text"]
)

report_gen_chain = prompt1 | model | parser

"""RunnableBranch(
    (condition_1, runnable_1),
    (condition_2, runnable_2),
    (condition_3, runnable_3),
    ...
    default_runnable
)"""

branch_chain = RunnableBranch(
    (
        lambda x: len(x.split()) > 300,
        prompt2 | model | parser,
    ),
    RunnablePassthrough(),
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({"topic": "Russia vs Ukraine"})

print(result)

print()
final_chain.get_graph().print_ascii()