from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.geometry("400x500")
root.title("slider")

def getme():
    print(f"i want this {myslider.get()} to win india")
    tmsg.showinfo("tell me bhai",f"i want this {myslider.get()} to win india")

def order():
    tmsg.showinfo("receved order ",f"we have received your order  {var.get()} Thank for ordering")
var  = IntVar()
Label(root,text="What would do you like to eat sir?",font="Lucida 15 bold").pack()

radio  = Radiobutton(root, text="Matar Paneer", padx=14, variable=var,value=1, font="Lucida 13 bold",foreground="red").pack(anchor="w")
radio  = Radiobutton(root, text="Coffee", padx=14, variable=var,value=2, font="Lucida 13 bold").pack(anchor="w")
radio  = Radiobutton(root, text="Rabdi", padx=14, variable=var,value=3, font="Lucida 13 bold").pack(anchor="w")
radio  = Radiobutton(root, text="Matar Paneer", padx=14, variable=var,value=4, font="Lucida 13 bold").pack(anchor="w")
radio  = Radiobutton(root, text="Matar Paneer", padx=14, variable=var,value=5, font="Lucida 13 bold").pack(anchor="w")
radio  = Radiobutton(root, text="Matar Paneer", padx=14, variable=var,value=6, font="Lucida 13 bold").pack(anchor="w")


Button(root,text="order now", command=order).pack()


Label(root, text="HOW MUCH %  YOU WANT INDIA WIN ").pack()
myslider = Scale(root, from_=0 , to= 100 , orient=HORIZONTAL)
myslider.pack()
Button(root,text="tell me", command=getme).pack()


root.mainloop()


