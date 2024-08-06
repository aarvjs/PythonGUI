from tkinter import *
root = Tk()
def hello():
   print("You are now hack by aarvjs")

root.geometry("500x600")
root.title("this is my first project") 

f1 = Frame(root, bg="green", borderwidth=3 ,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)

f2 = Frame(root ,bg="green",borderwidth=3,relief=SUNKEN)
f2.pack(fill=X)
# button start 

b1 = Button(root,text="hack now",bg="red" ,borderwidth=3,fg="white", command=hello)
b1.pack(anchor="w")


l = Label(f1 ,text="Kali Lunix   Hacker")
l.pack(side=LEFT)

l = Label(f2 ,text="I am a Hacker",fg="blue",font="Helvetica 19 bold")
l.pack()


root.mainloop()