# 🚀 Generative AI with LangChain: A Hands-On Journey

Welcome to my personal laboratory for Generative AI. This repository documents my ongoing journey of learning, experimenting, and building modern LLM-powered applications using **LangChain**.

Here, you will find code examples, detailed notes, and mini-projects covering the core concepts required to architect robust AI systems—from foundational prompt engineering to advanced Retrieval-Augmented Generation (RAG) and autonomous AI Agents.

---

## 📚 About This Repository

This repository serves as a comprehensive learning space where I explore the LangChain framework by implementing concepts from scratch and experimenting with various Large Language Models (LLMs) and AI frameworks.

**The primary objectives of this repository are to:**

- Master LangChain fundamentals and LLM application development.

- Explore the capabilities of different chat models and embedding models.

- Build semantic search systems and implement Retrieval-Augmented Generation (RAG).

- Develop autonomous AI Agents using LangChain.

- Architect and deploy real-world Generative AI applications.

The ultimate goal is to understand the entire lifecycle of modern AI application development, transforming raw models into practical, scalable tools.

---

## 📂 Repository Structure

The repository is organized chronologically and thematically to follow a logical learning progression.

```
Gen-AI
│
├── LangChain
│   ├── 01_LLM                 # Basic LLM integrations
│   ├── 02_Chat_Models         # Working with chat interfaces
│   ├── 03_Embedding_Models    # Vectorizing text data
│   ├── 04_Prompt_Templates    # Dynamic prompt generation
│   ├── 05_Structured_Output   # Extracting structured data
│   ├── 06_Output_Parsers      # Parsing LLM responses
│   ├── 07_Chains              # Linking components together
│   ├── 08_Runnables           # Introduction to LangChain Expression Language (LCEL)
│   ├── 09_Runnables_Part_2    # Advanced LCEL concepts
│   ├── 10_Document_Loaders    # Ingesting data from various sources
│   ├── 11_Text_Splitters      # Chunking documents for processing
│   ├── 12_Vector_Stores       # Storing and indexing embeddings
│   ├── 13_Retrievers          # Fetching relevant context
│   ├── 14_RAG                 # Retrieval-Augmented Generation basics
│   ├── 15_RAG_Project         # End-to-end RAG application
│   ├── 16_Tools               # Giving LLMs access to external functions
│   ├── 17_Tool_Calling        # Advanced function calling
│   └── 18_AI_Agents           # Building autonomous agents
│
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignored files and directories
└── README.md                  # This file
```

---

## 🎯 Learning Roadmap & Progress Tracker

The following roadmap tracks my progression through the core concepts of Generative AI and LangChain.

| Phase | Module | Status |
| --- | --- | --- |
| **Foundation** | Large Language Models (LLMs) | ✅ Completed |
| **Foundation** | Chat Models | ✅ Completed |
| **Foundation** | Embedding Models | ✅ Completed |
| **Data Ingestion** | Document Loaders | ⏳ In Progress |
| **Data Ingestion** | Text Splitters | ⏳ In Progress |
| **Data Ingestion** | Vector Stores | ⏳ In Progress |
| **Data Ingestion** | Retrievers | ⏳ In Progress |
| **Core Logic** | Prompt Templates | ⏳ In Progress |
| **Core Logic** | Structured Output | ⏳ In Progress |
| **Core Logic** | Output Parsers | ⏳ In Progress |
| **Core Logic** | Chains | ⏳ In Progress |
| **Core Logic** | Runnables & LCEL | ⏳ In Progress |
| **Advanced** | Retrieval-Augmented Generation (RAG) | ⏳ Planned |
| **Advanced** | Building RAG Applications | ⏳ Planned |
| **Advanced** | LangChain Tools | ⏳ Planned |
| **Advanced** | Tool Calling | ⏳ Planned |
| **Advanced** | AI Agents | ⏳ Planned |

---

## 🛠️ Technologies & Tools

This project leverages a diverse set of technologies to build and test Generative AI applications:

- **Programming Language:** Python

- **Framework:** LangChain

- **LLM Providers:** OpenAI, Groq, Google Gemini, Anthropic Claude, Hugging Face

- **NLP & Embeddings:** Sentence Transformers

- **Data Science:** NumPy, Scikit-Learn

- **Document Processing:** PyMuPDF

---

## ⚙️ Getting Started

Follow these steps to set up the project locally and start exploring the code.

### 1. Clone the Repository

```bash
git clone https://github.com/Div7anshKushwaha/Gen-AI.git
cd Gen-AI
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment to isolate dependencies.

```bash
uv venv
```

**For Windows:**

```bash
.venv\Scripts\activate
```

**For macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required packages using `uv` (or `pip` ):

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment Variables

Many of the examples require API keys for the respective LLM providers. Ensure you have a `.env` file in the root directory with the necessary keys (e.g., `OPENAI_API_KEY`, `GOOGLE_API_KEY`, etc.).

---

## 🚀 Future Plans

As I progress through the fundamentals, I plan to expand this repository to cover more advanced and production-ready topics:

- **LangGraph:** Building stateful, multi-actor applications with LLMs.

- **Model Context Protocol (MCP):** Standardizing context integration.

- **Multi-Agent Systems:** Architecting collaborative AI agents.

- **Fine-Tuning:** Customizing base models for specific domains.

- **AI Workflows:** Designing complex, automated processing pipelines.

- **Production-ready RAG Systems:** Implementing advanced RAG techniques (HyDE, query transformations, etc.).

- **End-to-End Projects:** Building full-stack Generative AI applications.

---

## 👨‍💻 Author

**Divyansh Kushwaha**

- **GitHub:** [Div7anshKushwaha](https://github.com/Div7anshKushwaha)

- **LinkedIn:** [Divyansh Kushwaha](https://www.linkedin.com/in/divyansh-kushwaha-33a56136a/)

---

⭐ *Feel free to explore the repository, star the project, and follow along with my Generative AI learning journey!*
