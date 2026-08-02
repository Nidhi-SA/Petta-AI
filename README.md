# Petta-AI 🧠  
A Multi‑Document Intelligence Assistant (v1.0 → v2.0 Evolution)

Petta‑AI is a personal document intelligence system that reads your files, understands your questions, and returns smart, contextual answers.  
It supports multiple file formats, performs semantic extraction, and provides a clean GUI for interactive querying.

This repository contains two major versions:

- v1.0 — Basic keyword search  
- v2.0 — Smart subject extraction, multi-format parsing, contextual search, FAISS indexing

Petta‑AI is designed as a practical demonstration of Python engineering, document parsing, and intelligent search — ideal for interviews, portfolio showcases, and real-world use.

##  Features (v2.0)

### Multi‑Format Document Reading  
Petta‑AI can read and search across:
- PDF  
- DOCX  
- TXT  
- PPT / PPTX  
- XLS / XLSX  
- PNG / JPG (OCR via Tesseract)

###  Smart Question Understanding  
Petta understands natural questions like:
- “Who is <string>”  
- “Where is Adelaide”  
- “Tell me about Python”  
- “Explain memory leak”  
- “Define machine learning”

It extracts the "subject" automatically — no manual rules needed.

### Contextual Search  
Returns meaningful context:
- 2 lines above  
- the matched line  
- 2 lines below  
With keyword highlighting.

###  FAISS Semantic Indexing  
Uses SentenceTransformers + FAISS for fast vector search.

###  GUI Interface  
Simple, clean Tkinter GUI for interactive querying.

##  How Petta Works (Architecture Overview)

┌──────────────────────────┐
│        User Query        │
└──────────────┬───────────┘
│
Subject Extraction
│
┌──────────────▼──────────────┐
│   Keyword + Semantic Search │
└──────────────┬──────────────┘
│
Multi‑Format Parser
┌──────────────┬──────────────┬──────────────┐
│ PDF Parser   │ DOCX Parser  │PPT/XLS Parser│
└──────────────┴──────────────┴──────────────┘
│
Context Window Builder
│
┌──────────────▼──────────────┐
│         GUI Output          │
└─────────────────────────────┘


##  Project Structure
Petta-AI/
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── data/
│   ├── sample.pdf
│   ├── sample.docx
│   ├── sample.txt
│   └── (add your documents here)
│
├── v1.0/
│   ├── agent_backend.py
│   ├── agent_gui.py
│
├── v2.0/
│   ├── agent_backendv2.py
│   ├── agent_guiv2.py

##  Installation

Clone the repository:

git clone https://github.com/Nidhi-SA/Petta-AI.git (github.com in Bing)
cd Petta-AI

## Install dependencies:
pip install -r requirements.txt

## Running Petta v2.0
python v2.0/agent_guiv2.py

## Place your documents inside the "data/" folder.

Ask Petta questions like:
- “Who is <string>”
- “Where is Adelaide”
- “Explain Python”
- “Tell me about memory leak”

##  Version Comparison

###  ---  v1.0 ---
- Basic keyword search  
- No subject extraction  
- Limited file support  
- Simple GUI  

###  ---  v2.0 ---
- Smart subject extraction  
- Multi-format parsing  
- Contextual search  
- FAISS semantic indexing  
- Cleaner GUI  
- More accurate answers  

##  Future Improvements
- Add CSV / JSON / HTML parsing  
- Add chat memory  
- Add colored highlighting in GUI  
- Add “Top 3 facts” summarizer  
- Add semantic ranking of results  
- Add web search integration  

##  License
This project is licensed under the MIT License — see the LICENSE file for details.

##  Author
Nidhi Sh  
Adelaide, South Australia  
2026