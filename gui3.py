
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("700x535")

def myfunc():
    print("click me bhai ")

def help():
    print("I will Help You")
    tmsg.showinfo("Helop","Aarv will help you")

def rate():
    print("rate according to you")
    val = tmsg.askquestion("was your experience good?")
    if val == "yes":
       msg = "Great. Rate us plese"
    else:
        msg = "Sorry for bad experience"
    tmsg.showinfo("expience",msg)

def view():
    print("zoom you screen")

# mymenu = Menu(root)

#  mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)

# root.config(menu=mymenu)

yourmenu = Menu(root)

m1 = Menu(yourmenu,tearoff=0)
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Open",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="File",menu=m1)


m2 = Menu(yourmenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Font Size",command=myfunc)
m2.add_command(label="Color",command=myfunc)
root.config(menu=yourmenu)
yourmenu.add_cascade(label="Edit",menu=m2)





m4 = Menu(yourmenu,tearoff=0)
m4.add_command(label="zoom",command=view)
m4.add_command(label="Status Bar",command=view)
yourmenu.add_cascade(label="View",menu=m4)
root.config(menu=yourmenu)

m3 = Menu(yourmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
yourmenu.add_cascade(label="Help",menu=m3)
root.config(menu=yourmenu)




root.mainloop()





