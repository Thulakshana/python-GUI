import tkinter as tk
from tkinter import messagebox
import pyodbc

# ---------------- Database Connection ----------------
def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=LAPTOP-OED5TH6H\\SQLEXPRESS;"
            "DATABASE=pr;"
            "Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None


# ---------------- Save Data Function ----------------
def save_data():
    name = name_entry.get()
    age = age_entry.get()

    if name == "" or age == "":
        messagebox.showwarning("Input Error", "Please enter both Name and Age")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO [user] (name, age) VALUES (?, ?)",
            (name, int(age))
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Data saved successfully")

        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Age must be a number")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- Tkinter Window ----------------
root = tk.Tk()
root.title("User Form")
root.geometry("400x300")
root.iconbitmap("abc.ico")

# ---------------- UI Components ----------------
tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

tk.Label(root, text="Age:", font=("Arial", 12)).pack(pady=5)
age_entry = tk.Entry(root, font=("Arial", 12))
age_entry.pack(pady=5)

tk.Button(
    root,
    text="OK",
    font=("Segoe UI", 12, "bold"),
    bg="#2ecc71",          # modern green
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    relief="flat",         # remove ugly border
    padx=20,
    pady=8,
    cursor="hand2",
    command=save_data
).pack(pady=20)

# ---------------- Run App ----------------
root.mainloop()
