import tkinter as tk
from tkinter import ttk

# ---------------- Window 1 ----------------
root = tk.Tk()
root.title("First Window")
root.geometry("400x400")

def open_second_window():
    root.destroy()  # close first window

    second = tk.Tk()   # create second window
    second.title("Second Window")
    second.geometry("400x400")

    label = ttk.Label(second, text="This is Second Window", font=("Arial", 16))
    label.pack(pady=40)

    second.mainloop()

btn = ttk.Button(root, text="Open Second Window", command=open_second_window)
btn.pack(expand=True)

root.mainloop()
