from tkinter import *
root=Tk()

l1=Label(root,text="Username")
l2=Label(root,text="EmailID")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b=Button(root,text="LOGIN")
b.grid(row=2,column=1)
