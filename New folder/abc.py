import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
import sys

CONFIG_FILE = "config.json"

# ---------------- Load Server ----------------
def load_server():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("server", "").strip()
        except json.JSONDecodeError:
            return ""
    return ""

# ---------------- Open Window Three ----------------
def open_window_three():
    subprocess.Popen(["python", "window_three.py"])
    sys.exit()   # CLOSE current program completely

# ---------------- Save Server ----------------
def save_server():
    server = server_entry.get().strip()

    if server == "":
        messagebox.showwarning("Input Error", "Server name cannot be empty")
        return

    with open(CONFIG_FILE, "w") as f:
        json.dump({"server": server}, f, indent=4)

    messagebox.showinfo("Success", "Server name saved successfully")
    open_window_three()

# ================= MAIN LOGIC =================

# 🔴 IMPORTANT: Check FIRST
existing_server = load_server()

if existing_server:
    # Server already exists → skip this window
    open_window_three()

# ================= TK WINDOW =================

root = tk.Tk()
root.title("Server Configuration")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="SQL Server Name", font=("Arial", 11)).pack(pady=10)

server_entry = tk.Entry(root, width=45)
server_entry.pack(pady=5)

tk.Button(
    root,
    text="Save & Continue",
    width=25,
    command=save_server
).pack(pady=20)

root.mainloop()
