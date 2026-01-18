import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("Stylish Tkinter")

# Fonts and colors
label = tk.Label(root, text="Enter Name:", font=("Helvetica", 14, "bold"), fg="white", bg="#34495e")
label.pack(pady=10, padx=10, fill="x")

entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=10, padx=10)

button = tk.Button(root, text="Submit", font=("Helvetica", 12, "bold"), bg="#2ecc71", fg="white", activebackground="#27ae60")
button.pack(pady=20)

root.mainloop()
