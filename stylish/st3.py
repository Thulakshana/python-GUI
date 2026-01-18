import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("500x400")
root.title("Styled Frames")

header_frame = tk.Frame(root, bg="#34495e", height=50)
header_frame.pack(fill="x")

tk.Label(header_frame, text="My App", fg="white", bg="#34495e", font=("Helvetica", 16, "bold")).pack(pady=10)

body_frame = tk.Frame(root, bg="#ecf0f1")
body_frame.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(body_frame, text="Name:", bg="#ecf0f1", font=("Helvetica", 12)).grid(row=0, column=0, pady=5)
tk.Entry(body_frame, font=("Helvetica", 12)).grid(row=0, column=1, pady=5, padx=10)

tk.Button(body_frame, text="Submit", bg="#2ecc71", fg="white", font=("Helvetica", 12, "bold")).grid(row=1, columnspan=2, pady=20)

root.mainloop()
