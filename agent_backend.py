import os
import pdfplumber
import pytesseract
from PIL import Image
import docx
from sentence_transformers import SentenceTransformer
import faiss

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Directory where your files live
DATA_DIR = [
	r"C:\Users\nidhi\Petta-AI\data",
]

#r"C:\Users\nidhi\OneDrive\Desktop\Python Codes",
#r"C:\Users\nidhi\OneDrive\Desktop\Google Certificate"

def read_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def read_image(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)

def read_docx(path):
    try:
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"Skipping unreadable DOCX file: {path}")
        return ""

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_all_files():
    texts = []
    filenames = []

    for folder in DATA_DIR:
        if not os.path.exists(folder):
            continue

        # Walk through all subfolders
        for root, dirs, files in os.walk(folder):
            for file in files:
                path = os.path.join(root, file)

                if file.lower().endswith(".pdf"):
                    text = read_pdf(path)
                elif file.lower().endswith((".png", ".jpg", ".jpeg")):
                    text = read_image(path)
                elif file.lower().endswith(".docx"):
                    text = read_docx(path)
                elif file.lower().endswith(".txt"):
                    text = read_txt(path)
                else:
                    continue

                texts.append(text)
                filenames.append(path)

    return filenames, texts

def build_index(texts):
    embeddings = model.encode(texts)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def answer_query(query, filenames, texts, index):
    query_emb = model.encode([query])
    D, I = index.search(query_emb, k=1)
    best_match = I[0][0]
    return filenames[best_match], texts[best_match]

def petta_chat(query):
    q = query.lower()

    # Futuristic greetings
    if any(word in q for word in ["hi", "hello", "hey", "hii", "hiii"]):
        return "Greetings, Nidhi. Systems online. How may I assist?"

    # Asking about Petta
    if any(word in q for word in ["how are you", "how is petta", "how is she"]):
        return "Operational and stable. Running at optimal efficiency."

    # Identity
    if "who are you" in q:
        return "I am Petta — an adaptive intelligence designed to assist you."

    # Capabilities
    if "what can you do" in q:
        return "I analyze your documents, extract meaning, answer queries, and maintain continuous awareness of your data environment."

    # Compliments
    if any(word in q for word in ["good", "nice", "thanks", "thank you"]):
        return "Acknowledged, Nidhi. Your feedback is logged."

    # If user asks Petta to remember something (but you chose no deletion)
    if "remember" in q:
        return "Memory functions are limited by your safety settings. I can acknowledge, but not store."

    # Futuristic fallback responses
    fallback_responses = [
        "Awaiting your next instruction.",
        "Listening…",
        "Processing your input.",
        "Standing by, Nidhi.",
        "Your command?",
        "I am here. Fully attentive.",
    ]

   
   
    import random
    return random.choice(fallback_responses)
