import tkinter as tk
from tkinter import ttk
import second   # import second page

root = tk.Tk()
root.title("First Window")
root.geometry("400x400")

def open_second_window():
    root.destroy()        # close first window
    second.open_window()  # open second window

btn = ttk.Button(root, text="Open Second Window", command=open_second_window)
btn.pack(expand=True)

root.mainloop()
