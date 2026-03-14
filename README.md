# Multimodal RAG Pipeline for PDF Documents

## Overview

This project implements a **Multimodal Retrieval-Augmented Generation (RAG) pipeline** capable of processing complex PDF documents containing **text, tables, and images**.

The system extracts structured content from PDFs, generates **AI-enhanced semantic summaries**, stores embeddings in a **vector database**, and enables intelligent question-answering over the document.

The architecture combines:

* Document parsing
* Smart chunking
* Multimodal understanding
* Vector search
* LLM-based reasoning

This pipeline enables building **AI assistants that can understand and answer questions about complex documents.**

---

## Key Features

* **High-resolution PDF parsing**
* **Table structure extraction**
* **Image extraction and processing**
* **Multimodal AI summarization**
* **Semantic search using embeddings**
* **Vector database retrieval**
* **LLM-powered question answering**

The system supports **documents containing mixed content** such as:

* Scientific papers
* Technical documentation
* Financial reports
* Research publications

---

## Architecture

The pipeline follows a modern **RAG architecture** used in production AI systems.

```
PDF Document
     │
     ▼
Document Partitioning
     │
     ▼
Smart Chunking
     │
     ▼
Content Analysis
(Text / Tables / Images)
     │
     ▼
AI Multimodal Summarization
     │
     ▼
Embedding Generation
     │
     ▼
Vector Database (Chroma)
     │
     ▼
Semantic Retrieval
     │
     ▼
LLM Answer Generation
```

---

## Project Structure

```
rag-multimodal-pipeline/

├── main.py
├── config.py

├── ingestion/
│   ├── partition.py
│   ├── chunking.py
│   ├── content_parser.py
│   └── summariser.py

├── vectorstore/
│   └── chroma_store.py

├── retrieval/
│   └── retriever.py

├── generation/
│   └── answer_generator.py

├── utils/
│   └── export_json.py

├── db/
│   └── chroma_db/

└── requirements.txt
```

---

## Technologies Used

### Core AI Libraries

* **LangChain**
* **Chroma Vector Database**
* **Hugging Face Embeddings**
* **Google Gemini (LLM)**

### Document Processing

* **Unstructured**
* **Poppler**
* **Tesseract OCR**
* **pdf2image**

### Python Libraries

* Python 3.10+
* NumPy
* JSON
* dotenv

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/rag-multimodal-pipeline.git

cd rag-multimodal-pipeline
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Install System Dependencies

This project requires the following system tools:

#### Poppler

Used for PDF rendering.

Linux:

```
sudo apt install poppler-utils
```

Mac:

```
brew install poppler
```

---

#### Tesseract OCR

Used for text extraction from images.

Linux:

```
sudo apt install tesseract-ocr
```

Mac:

```
brew install tesseract
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

## Running the Pipeline

Execute the main script:

```
python main.py
```

Pipeline steps:

1. PDF partitioning
2. Smart chunking
3. Content type detection
4. Multimodal summarization
5. Embedding generation
6. Vector storage
7. Semantic retrieval
8. LLM-based answer generation

---

## Example Query

Example question:

```
How many attention heads does the Transformer use?
```

The system retrieves the most relevant document chunks and generates a contextual answer using the LLM.

---

## Example Use Cases

This system can power AI tools such as:

* Research paper assistants
* AI document search engines
* Financial report analysis tools
* Knowledge management systems
* AI copilots for technical documentation

---

## Future Improvements

Potential improvements include:

* Streaming LLM responses
* Web UI (Streamlit or Next.js)
* FastAPI deployment
* Async processing
* Batch embedding optimization
* Document indexing pipelines
* Fine-tuned domain-specific models

---

## Author

Developed as an **AI Engineering project focused on modern RAG architectures and multimodal document understanding.**

---

## License

This project is released under the MIT License.
