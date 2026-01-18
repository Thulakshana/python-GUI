import tkinter as tk 
from tkinter import ttk

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('400x400') #width and height 

check1_var=tk.StringVar()
check2_var=tk.StringVar()

def check_res():
    print(check1_var.get())
    print(check2_var.get())


check1=ttk.Checkbutton(root,text='python',variable=check1_var,onvalue="python")
check1.pack()

check2=ttk.Checkbutton(root,text='java',variable=check2_var,onvalue="java")
check2.pack()


button=ttk.Button(root,text="click me",command=check_res)
button.pack()


root.mainloop()