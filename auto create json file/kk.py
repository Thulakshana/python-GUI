import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess

CONFIG_FILE = "config.json"

# ---------------- Load Server ----------------
def load_server():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return ""
                data = json.loads(content)
                return data.get("server", "")
        except (json.JSONDecodeError, ValueError):
            return ""
    return ""

# ---------------- Save Server ----------------
def save_server():
    server = server_entry.get().strip()

    if server == "":
        messagebox.showwarning("Input Error", "Server name cannot be empty")
        return

    # Create config.json if not exist
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({"server": server}, f, indent=4)
        messagebox.showinfo("Saved", "Server name saved successfully")
        open_window_three()
        root.destroy()
        return

    # If file exists, check if server already stored
    existing_server = load_server()
    if existing_server != "":
        messagebox.showinfo("Info", "Server name already exists")
        open_window_three()
        root.destroy()
        return

    # Otherwise save the server
    with open(CONFIG_FILE, "w") as f:
        json.dump({"server": server}, f, indent=4)
    messagebox.showinfo("Saved", "Server name saved successfully")
    open_window_three()
    root.destroy()

# ---------------- Open Window Three ----------------
def open_window_three():
    # Make sure window_three.py is in the same folder
    subprocess.Popen(["python", "window_three.py"])

# ---------------- Tkinter UI ----------------
root = tk.Tk()
root.title("Server Configuration")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="SQL Server Name", font=("Arial", 11)).pack(pady=8)

server_entry = tk.Entry(root, width=45)
server_entry.pack(pady=5)

# Pre-fill server if exists
server_entry.insert(0, load_server())

tk.Button(root, text="OK / Save Server", width=25, command=save_server).pack(pady=20)

root.mainloop()
