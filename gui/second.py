import tkinter as tk
from tkinter import ttk

def open_window():
    second = tk.Tk()
    second.title("Second Window")
    second.geometry("400x400")

    label = ttk.Label(second, text="This is Second Window", font=("Arial", 16))
    label.pack(pady=40)

    second.mainloop()
