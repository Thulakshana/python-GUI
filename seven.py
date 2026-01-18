import tkinter as tk 
from tkinter import ttk
from calendar import month_name
#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

month_names=[month_name[i] for i in range(1,13)]
print(month_names)

comb=ttk.Combobox(root,values=['python','java','c++'])
comb.pack()

label=ttk.Label(root,textvariable=comb.get())
label.pack()





root.mainloop()