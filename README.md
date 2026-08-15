# 🤖 Gen-AI

A hands-on learning repository covering **Generative AI application development with LangChain** — from raw LLM calls to prompt engineering, RAG, tool calling, and AI agents.

## 📌 About

This repository contains my personal, code-first exploration of LangChain and the broader Generative AI stack. Every folder corresponds to a core LangChain concept, implemented and run as standalone scripts or notebooks rather than copied from documentation.

The repository is organized **topic-wise** so each concept — models, prompts, chains, retrieval, agents, and so on — can be studied and run independently of the others.

## 🧠 Topics Covered

| Topic | What is Covered |
| --- | --- |
| **Models** | Direct LLM calls via Groq (`llama-3.3-70b-versatile`), Hugging Face inference endpoints (Mistral-7B-Instruct), and fully local inference with a Hugging Face pipeline (TinyLlama-1.1B) |
| **Embedding Models** | Hugging Face sentence-transformer embeddings (`all-MiniLM-L6-v2`, `all-mpnet-base-v2`, `BAAI/bge-small-en-v1.5`) and a cosine-similarity document search demo |
| **Prompts** | `PromptTemplate` and `ChatPromptTemplate`, `MessagesPlaceholder` for chat history, a saved/reloaded prompt template (`template.json`), and a Streamlit research-paper summarizer UI |
| **Chains** | Simple, sequential, parallel (`RunnableParallel`), and conditional (`RunnableBranch`) chains built with LCEL |
| **Output Parsers** | `StrOutputParser`, `JsonOutputParser`, `PydanticOutputParser`, and a legacy `StructuredOutputParser` example kept for comparison against modern parsers |
| **Structured Output** | `model.with_structured_output()` using a `TypedDict`, a Pydantic model, and a raw JSON schema |
| **Runnables** | `RunnableSequence`, `RunnableParallel`, `RunnablePassthrough`, `RunnableLambda`, `RunnableBranch` — the LCEL primitives, used both standalone and inside the RAG pipeline |
| **Document Loaders** | `CSVLoader`, `DirectoryLoader` + `PyPDFLoader`, `PyPDFLoader`, `TextLoader`, `WebBaseLoader`, plus the YouTube Transcript API used directly for the RAG pipeline |
| **Text Splitters** | Length-based (`CharacterTextSplitter`), text-structure-based (`RecursiveCharacterTextSplitter`), document-structure-based splitting for Markdown/Python (`Language` enum), and embedding-based semantic chunking (`SemanticChunker`) |
| **Vector Stores** | Chroma (persisted locally to `my_chroma_db`) and FAISS, including add/update/delete and metadata filtering on Chroma |
| **Retrievers** | Vector store retriever, MMR retriever, multi-query retriever, contextual compression retriever (LLM-based), and the built-in Wikipedia retriever |
| **RAG** | A full YouTube-transcript question-answering pipeline: transcript fetch → chunk → embed → FAISS store → retrieve → LCEL chain → Groq LLM answer |
| **Tool Calling** | Manual `bind_tools()` + tool-call loop for a multiply tool, then a two-step currency conversion tool chain (ExchangeRate-API) using `InjectedToolArg` |
| **Tools** | Built-in tools (`DuckDuckGoSearchRun`, `ShellTool`), three ways to build custom tools (`@tool`, `StructuredTool.from_function`, a `BaseTool` subclass), and a simple custom `Toolkit` |
| **AI Agents** | A `create_agent` (LangChain 1.x agent API) ReAct-style agent combining DuckDuckGo search with a custom Weatherstack weather tool |

## 📂 Repository Structure

```text
Gen-AI/
│
├── Chains_in_Langchain/
│   ├── simple_chain.py
│   ├── sequential_chain.py
│   ├── parallel_chains.py
│   └── conditional_chains.py
│
├── Langchain_AI_Agents/
│   └── AI_Agents.ipynb              # create_agent + search + weather tool
│
├── Langchain_Document_Loaders/
│   ├── csv_loader.py
│   ├── directory_loader.py
│   ├── pdf_loader.py
│   ├── text_loader.py
│   ├── webbase_loader.py
│   ├── ML.pdf / cricket.txt         # sample data used by the loaders
│
├── Langchain_Models/
│   ├── 1.LLM/                       # raw LLM completion
│   ├── 2.ChatModels/                # Groq, HF endpoint, local HF pipeline
│   └── 3.EmbeddingModels/           # embeddings + similarity search
│
├── Langchain_Output_Parsers/
├── Langchain_Prompts/
│   └── prompt_ui.py                 # Streamlit research-paper summarizer
│
├── Langchain_RAG/
│   └── rag_using_langchain.ipynb    # YouTube transcript RAG pipeline
│
├── Langchain_Retreivers/
├── Langchain_Runnables/
├── Langchain_Structured_Output/
├── Langchain_Text_Splitters/
├── Langchain_Tool_calling/
│   └── tool_calling.ipynb
├── Langchain_Tools/
│   └── tools_in_langchain.ipynb
├── Langchain_Vector_Stores/
│   ├── chroma_vector_stores.py
│   └── my_chroma_db/                # persisted Chroma collection
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

> Note: the retrievers folder is spelled `Langchain_Retreivers` in the repository itself — kept as-is here to match the actual path.

## 🔧 Technologies & Libraries

Based on what's imported and actually exercised in the code:

- **Language:** Python
- **Framework:** LangChain (`langchain`, `langchain-core`, `langchain-community`, `langchain-text-splitters`, `langchain-experimental`, `langchain_classic` for `MultiQueryRetriever` / `ContextualCompressionRetriever`), plus the newer `langchain.agents.create_agent` API
- **LLM provider actually used at runtime:** **Groq** (`langchain-groq`, model `llama-3.3-70b-versatile`, and `openai/gpt-oss-120b` in one parallel-chains example)
- **Hugging Face:** `langchain-huggingface` for both a hosted inference endpoint (`HuggingFaceEndpoint`, Mistral-7B-Instruct) and fully local inference (`HuggingFacePipeline`, TinyLlama-1.1B); `sentence-transformers` embedding models used throughout
- **Vector stores:** Chroma (`langchain-chroma` / `chromadb`) and FAISS (`faiss-cpu`)
- **Other integrations exercised in code:** `youtube-transcript-api` (RAG source data), `DuckDuckGoSearchRun` (web search tool), Weatherstack API and ExchangeRate-API (custom agent/tool calls), `pymupdf`/`pypdf` (PDF loading), `streamlit` (the prompt UI)
- **Not currently used in any script**, despite being listed in `requirements.txt`: `openai`, `google-generativeai`, `langchain-openai`, `langchain-anthropic`, `langchain-google-genai`. These are installed as available dependencies but no example in the repo calls OpenAI, Gemini, or Anthropic models yet.

## ⚙️ Installation

```bash
git clone https://github.com/Div7anshKushwaha/Gen-AI.git
cd Gen-AI
```

Create and activate a virtual environment:

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**
```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables / API Keys

Based on the code, the keys actually read from the environment are:

| Variable | Used by |
| --- | --- |
| `GROQ_API_KEY` | Every `ChatGroq` example — Models, Chains, Output Parsers, Runnables, Retrievers, RAG, Tool Calling, AI Agents |
| `WEATHERSTACK_API_KEY` | `get_weather_data` tool in `Langchain_AI_Agents/AI_Agents.ipynb` |
| `EXCHANGE_RATE_API_KEY` | `get_conversion_factor` tool in `Langchain_Tool_calling/tool_calling.ipynb` |

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
WEATHERSTACK_API_KEY=your_api_key_here
EXCHANGE_RATE_API_KEY=your_api_key_here
```

The Hugging Face endpoint example (`2_chatmodels_hf.py`) will also need a Hugging Face access token available to `huggingface_hub` (e.g. `HUGGINGFACEHUB_API_TOKEN`) if you run it against the hosted inference API; the local pipeline example (`3_chatmodels_hf_locally.py`) needs no key at all.

**Never commit API keys or `.env` files to GitHub.**

## ▶️ Running the Examples

Most examples are standalone scripts — navigate into the relevant folder and run the file directly:

```bash
cd Langchain_Models/2.ChatModels
python 1_chatmodels_groq.py
```

Some files reference **absolute local paths** (e.g. `Langchain_Document_Loaders/csv_loader.py` and `Langchain_Text_Splitters/length_bases_splitting.py` point at paths under `C:\Users\divya\...`) — update these paths to your own files before running them.

The notebooks (`Langchain_RAG/rag_using_langchain.ipynb`, `Langchain_Tool_calling/tool_calling.ipynb`, `Langchain_Tools/tools_in_langchain.ipynb`, `Langchain_AI_Agents/AI_Agents.ipynb`) are meant to be run cell-by-cell in Jupyter or VS Code, since several install packages inline with `%pip install` / `!pip install`.

The Streamlit prompt UI can be launched with:

```bash
cd Langchain_Prompts
streamlit run prompt_ui.py
```

## 📚 Learning Roadmap

```text
Models
   ↓
Prompts
   ↓
Chains
   ↓
Output Parsers
   ↓
Structured Output
   ↓
Runnables (LCEL)
   ↓
Document Loaders
   ↓
Text Splitters
   ↓
Vector Stores
   ↓
Retrievers
   ↓
RAG
   ↓
Tools
   ↓
Tool Calling
   ↓
AI Agents
```

## 🔍 Concepts Explained

**Models** — The foundation layer: calling an LLM directly (Groq), through a hosted Hugging Face endpoint, and fully locally with a Hugging Face pipeline. Useful for understanding provider trade-offs before wrapping models in chains.

**Prompts** — `PromptTemplate` for single-turn prompts and `ChatPromptTemplate` with `MessagesPlaceholder` for multi-turn chat context. Demonstrated with a saved/reloadable template and a small Streamlit front-end.

**Chains** — LCEL's `|` operator used to compose prompt → model → parser pipelines, extended into sequential, parallel, and conditional (branching) flows.

**Output Parsers & Structured Output** — Turning free-text LLM output into strings, JSON, or validated Pydantic/TypedDict objects, including a look at the deprecated `StructuredOutputParser` for contrast with the current `with_structured_output()` API.

**Runnables** — The composable building blocks (`Sequence`, `Parallel`, `Passthrough`, `Lambda`, `Branch`) that LCEL and the RAG chain are built on.

**Document Loaders & Text Splitters** — Getting external data (CSV, PDF, text files, web pages, YouTube transcripts) into LangChain `Document` objects, then chunking them by length, structure, or semantic similarity.

**Vector Stores & Retrievers** — Storing embedded chunks in Chroma or FAISS, then retrieving them back via plain similarity search, MMR (diversity-aware), multi-query (LLM-expanded queries), contextual compression (LLM-filtered), or Wikipedia lookup.

**RAG** — Combining the above into a working system: fetch a YouTube transcript, split and embed it, store it in FAISS, retrieve relevant chunks for a question, and generate a grounded answer with Groq.

**Tools & Tool Calling** — Defining functions the LLM can call (`@tool`, `StructuredTool`, `BaseTool`), binding them to a model with `bind_tools()`, and manually running the tool-call → tool-result → final-answer loop, including a multi-step currency conversion example.

**AI Agents** — Using LangChain's `create_agent` to let the LLM autonomously decide which tool to call (web search vs. a custom weather API) and in what order.

## 🧪 Examples

| Example | Concept | Key Technologies | What it teaches |
| --- | --- | --- | --- |
| `Langchain_Prompts/prompt_ui.py` | Prompts | Streamlit, `PromptTemplate.save/load` | Building a small interactive UI around a reusable prompt template |
| `Langchain_RAG/rag_using_langchain.ipynb` | RAG | YouTube Transcript API, FAISS, `BAAI/bge-small-en-v1.5`, Groq | A complete indexing → retrieval → generation pipeline over unstructured video transcripts |
| `Langchain_Retreivers/contextual_compression_retriever.py` | Retrievers | FAISS, `LLMChainExtractor` | Using an LLM to filter retrieved chunks down to only the relevant sentences |
| `Langchain_Tool_calling/tool_calling.ipynb` | Tool Calling | ExchangeRate-API, `InjectedToolArg` | Chaining two tool calls together (fetch a rate, then apply it) without re-exposing the intermediate value to the LLM |
| `Langchain_AI_Agents/AI_Agents.ipynb` | AI Agents | `create_agent`, DuckDuckGo, Weatherstack API | An agent that reasons over a multi-step question and picks the right tool at each step |

## 🗺️ RAG Pipeline

```text
YouTube Video
    ↓
YouTube Transcript API
    ↓
RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200)
    ↓
HuggingFace Embeddings (BAAI/bge-small-en-v1.5)
    ↓
FAISS Vector Store
    ↓
Similarity Retriever (k=20)
    ↓
Relevant Context
    ↓
Groq LLM (llama-3.3-70b-versatile)
    ↓
Answer
```

## 🤖 AI Agent Architecture

```text
User Query
 ↓
create_agent (LangChain 1.x agent)
 ↓
Reasoning over available tools
 ↓
Tool Selection (DuckDuckGo search or get_weather_data)
 ↓
Tool Execution
 ↓
Observation fed back to the LLM
 ↓
Final Response
```

## 📈 Learning Progress

- [x] LangChain Models (Groq, Hugging Face hosted & local)
- [x] Prompt Templates
- [x] Chains (simple, sequential, parallel, conditional)
- [x] Output Parsers
- [x] Structured Output
- [x] Runnables / LCEL
- [x] Document Loaders
- [x] Text Splitters
- [x] Vector Stores
- [x] Retrievers
- [x] RAG
- [x] Tool Calling
- [x] Tools
- [x] AI Agents

## 🚀 Future Improvements

Currently implemented: single-turn RAG, single-agent tool use, and manual tool-calling loops.

Realistic next steps for this repository:

- Conversation memory across chain/agent turns
- Agentic RAG (retrieval as a tool the agent decides to call)
- Multi-agent systems
- LangGraph for stateful, graph-based workflows
- Basic evaluation of RAG/agent outputs
- Actually exercising the already-installed OpenAI/Gemini/Anthropic integrations for provider comparison
- Deployment of at least one project (currently all examples are local scripts/notebooks)

## 👨‍💻 Author

**Divyansh Kushwaha**

Pursuing a **BS in Data Science and Applications from IIT Madras**, with a focus on **AI Engineering, Generative AI, and Machine Learning**.

- GitHub: [Div7anshKushwaha](https://github.com/Div7anshKushwaha)
- LinkedIn: [Divyansh Kushwaha](https://www.linkedin.com/in/divyansh-kushwaha-603616383)

## ⭐ Repository Goals

This repository is primarily a hands-on learning resource, not a production system — it exists to document a structured path through LangChain and Generative AI application development, and will keep growing as new concepts and projects are added.

If you're on a similar learning path, feel free to explore the code, open an issue, or star the repo. ⭐
