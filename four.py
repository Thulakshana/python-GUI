import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello World")
root.geometry("400x400")

class PageOne(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        # Entry (left)
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, padx=(20, 5), pady=20, sticky="ew")

        # Button (right)
        self.button = ttk.Button(
            self,
            text="Click",
            command=self.button_click
        )
        self.button.grid(row=0, column=1, padx=(5, 20), pady=20)

        # Label (below)
        self.label = ttk.Label(self)
        self.label.grid(row=1, column=0, columnspan=2, pady=20)

    def button_click(self):
        value = self.entry.get()
        self.label.config(text=value)

page1 = PageOne(root)
page1.pack(fill="both", expand=True)

root.mainloop()
