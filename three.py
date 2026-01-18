import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello World")
root.geometry("400x400")

class PageOne(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure grid to center content
        self.columnconfigure(0, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, pady=20)

        self.button = ttk.Button(
            self,
            text="Click Me",
            command=self.button_click
        )
        self.button.grid(row=1, column=0, pady=30)

        self.label = ttk.Label(self)
        self.label.grid(row=2, column=0, pady=40)

    def button_click(self):
        value = self.entry.get()
        self.label.config(text=value)

page1 = PageOne(root)
page1.pack(fill="both", expand=True)

root.mainloop()
