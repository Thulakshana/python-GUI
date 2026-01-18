import tkinter as tk 
from tkinter import ttk

#create window
root=tk.Tk()

root.title("hello world")

root.iconbitmap("abc.ico")

root.geometry('500x400') #width and height 

table=ttk.Treeview(root,columns=('name','age','email'),show='headings')
table.heading('name',text='Name')
table.heading('age',text='Age')
table.heading('email',text='Email')
table.column('age',width=100)
table.pack()



#table.insert('',0,values=('kamal',23,'kkk@gmail.com'))
name=['kamal','sita','gita','ram']
age=[23,21,22,24]

for idx,value in enumerate(name):
    table.insert('',idx,values=(name[idx],age[idx],f'{name[idx]}@gmail.com'))

def selected_item(event):
    print(table.item(table.selection())['values'])

table.bind('<<TreeviewSelect>>',lambda event:selected_item(event))


root.mainloop()