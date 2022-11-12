import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.configure(bg="blue")
app.geometry("270x480")
app.resizable(False, False)
app.title("AppAn")

# Frame input
input_frame = ttk.Frame(app)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

app.mainloop()
