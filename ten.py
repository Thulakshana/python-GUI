import tkinter as tk
from tkinter import ttk

# create window
root = tk.Tk()
root.title("hello world")
root.geometry("400x400")

# progress bar
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate"
)
progress.pack(pady=50)

progress["maximum"] = 100
progress["value"] = 0

def fill_progress():
    if progress["value"] < 100:
        progress["value"] += 1
        root.after(50, fill_progress)  # 50 ms × 100 = 5 seconds

# start filling automatically
fill_progress()

root.mainloop()
