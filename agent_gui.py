import os
import sys
import tkinter as tk

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agent_backend import load_all_files, build_index, answer_query

def refresh_index():
    global filenames, texts, index
    filenames, texts = load_all_files()
    index = build_index(texts)

refresh_index()

def petta_chat(query):
    return "Sorry, I don't have an answer for that. Please try another question."

def run_query():
    refresh_index()  # auto-refresh before every search
    query = entry.get()
    _, answer = answer_query(query, filenames, texts, index)
    if not answer or answer.strip() == "":
        answer = petta_chat(query)
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Petta: {answer}\n\n")

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
entry = tk.Entry(root, width=80)
entry.pack()

## trigger search on pressing Enter key
entry.bind("<Return>", lambda event: run_query())

## Modern icon button
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
output.insert(tk.END, "Petta: Hello Nidhi, I'm online and ready.\n\n")
scrollbar = tk.Scrollbar(root, command=output.yview)
output.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

root.mainloop()
