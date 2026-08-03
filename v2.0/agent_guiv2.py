import os
import sys
import tkinter as tk
import subprocess
import platform

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent_backendv2 import load_all_documents, build_faiss_index, hybrid_search

# Load documents + build index once at startup
filenames, texts = load_all_documents()
index = build_faiss_index(texts)

def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.call(["open", path])
    else:  # Linux
        subprocess.call(["xdg-open", path])

def refresh_index():
    global filenames, texts, index
    filenames, texts = load_all_documents()
    index = build_faiss_index(texts)

def run_query():
    refresh_index()
    query = entry.get().strip()

    if not query:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Petta: Please enter a question.\n\n")
        return

    answer = hybrid_search(query, filenames, texts, index)
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Petta:\n\n")

    # Loop through each block of the answer
    for block in answer.split("\n\n"):
        if block.strip() == "":
            continue

        # Detect filename line: [path]
        if block.startswith("[") and "]" in block:
            raw = block.split("]")[0].replace("[", "").strip()
            # filename cleaner
            for ext in [".pdf", ".docx", ".pptx", ".xlsx", ".xls", ".txt"]:
                if raw.lower().endswith(ext):
                    filename = raw
                    break
                if ext in raw.lower():
                    filename = raw.lower().split(ext)[0] + ext
                    break
            else:
                filename = raw.split(" (")[0].strip()

            # Show filename
            output.insert(tk.END, block + "\n")

            # Insert Open File button immediately AFTER filename
            btn = tk.Button(
                output,
                text="Open File",
                fg="#0066cc",
                bg="#ffffff",
                relief="flat",
                command=lambda f=filename: open_file(f)
            )
            output.window_create(tk.END, window=btn)

            # Space BEFORE slide text
            output.insert(tk.END, "\n\n")

        else:
            # Normal text (slide text)
            output.insert(tk.END, block + "\n\n")


root = tk.Tk()
root.title("Petta - Your AI Companion")
root.geometry("900x600")
root.configure(bg="#ffffff")

header = tk.Label(
    root,
    text="Petta is listening...",
    font=("Segoe UI", 16, "bold"),
    bg="#ffffff",
    fg="#444444",
    pady=10
)
header.pack(fill="x")

tk.Label(root, text="Ask your question:").pack()
entry = tk.Entry(root, width=90, font=("Segoe UI", 12))
entry.pack()

entry.bind("<Return>", lambda event: run_query())

search_btn = tk.Button(
    root,
    text="🔍",
    font=("Segoe UI Emoji", 16),
    bg="#ffffff",
    fg="#333333",
    relief="flat",
    command=run_query
)
search_btn.pack(pady=5)

output = tk.Text(
    root,
    wrap="word",
    font=("Segoe UI", 12),
    bg="#f7f7f7",
    fg="#333333",
    relief="flat",
    padx=10,
    pady=10
)
output.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(root, command=output.yview)
output.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

output.insert(tk.END, "Petta: Hello Nidhi, I'm online and ready.\n\n")



root.mainloop()
