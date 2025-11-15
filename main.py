import fitz  # PyMuPDF
import pyttsx3
import tkinter as tk
from tkinter.filedialog import askopenfilename
import threading

def read_pdf():
    file = askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return

    def speak_pdf():
        doc = fitz.open(file)
        engine = pyttsx3.init()
        for page in doc:
            text = page.get_text()
            if text.strip():
                engine.say(text)
                engine.runAndWait()

    threading.Thread(target=speak_pdf, daemon=True).start()

def close_app():
    root.destroy()

# GUI
root = tk.Tk()
root.title("PDF Reader")
root.geometry("300x250")

tk.Label(root, text="Click below to select a PDF", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Open PDF", command=read_pdf, font=("Arial", 12), bg="lightblue").pack(pady=5)
tk.Button(root, text="Close", command=close_app, font=("Arial", 12), bg="lightcoral").pack(pady=5)

root.mainloop()
