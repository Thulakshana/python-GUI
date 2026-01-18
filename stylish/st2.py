import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("TTK Stylish App")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="white", background="#1abc9c", padding=10)
style.configure("TLabel", font=("Arial", 12))

label = ttk.Label(root, text="Welcome to Stylish Tkinter!")
label.pack(pady=20)

button = ttk.Button(root, text="Click Me")
button.pack(pady=20)

root.mainloop()
