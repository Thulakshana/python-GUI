import tkinter as tk
from tkinter import messagebox
import pyodbc
import json
import os

CONFIG_FILE = "config.json"

# ---------------- Load Server (SAFE) ----------------
def load_server():
    if not os.path.exists(CONFIG_FILE):
        # File doesn't exist → create default
        with open(CONFIG_FILE, "w") as f:
            json.dump({"server": ""}, f)
        return ""
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read().strip()
            if not content:  # file is empty
                return ""
            data = json.loads(content)
            return data.get("server", "")
    except (json.JSONDecodeError, ValueError):
        # file invalid → reset to default
        with open(CONFIG_FILE, "w") as f:
            json.dump({"server": ""}, f)
        return ""

# ---------------- Save Server ----------------
def save_server():
    server = server_entry.get().strip()
    if server == "":
        messagebox.showwarning("Input Error", "Server name cannot be empty")
        return

    with open(CONFIG_FILE, "w") as f:
        json.dump({"server": server}, f, indent=4)

    messagebox.showinfo("Saved", "Server name saved permanently")

# ---------------- Database Connection ----------------
def get_connection():
    server = load_server()
    if server == "":
        messagebox.showerror("Error", "Server not configured")
        return None
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={server};"
            f"DATABASE=pr;"
            f"Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None

# ---------------- Tkinter UI ----------------
root = tk.Tk()
root.title("Database Configuration")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="SQL Server Name", font=("Arial", 11)).pack(pady=8)

server_entry = tk.Entry(root, width=45)
server_entry.pack(pady=5)

# Load saved server safely
server_entry.insert(0, load_server())

tk.Button(root, text="Save Server", width=20, command=save_server).pack(pady=10)

# ---------------- Test Button ----------------
def test_connection():
    conn = get_connection()
    if conn:
        messagebox.showinfo("Success", "Database connected successfully")
        conn.close()

tk.Button(root, text="Test Connection", width=20, command=test_connection).pack()

root.mainloop()
