from tkinter import *
root = Tk()

def getvals():
    print("submited by user")
    print(f"{namevalue.get(), passwordvalue.get(), adressvalue.get(),gendervalue.get()}")

with open("aarv.txt","a") as f:
    pass
    # f.write(f"{namevalue.get(), passwordvalue.get(), adressvalue.get(),gendervalue.get()}")



root.geometry("800x800")


Label(root, text="This is submit form" ,font="Helvetica 19 bold").grid(row=0, column=3)

name  = Label(root, text="Name")
password  = Label(root, text="Password")
adress  = Label(root, text="Adress")
gender  = Label(root, text="Gender")

name.grid(row=1, column=2)
password.grid(row=2, column=2)
adress.grid(row=3, column=2)
gender.grid(row=4, column=2)

namevalue = StringVar()
passwordvalue = StringVar()
adressvalue = StringVar()
gendervalue = StringVar()

nameentery = Entry(root,textvariable=namevalue)
passwordentery = Entry(root,textvariable=passwordvalue)
adressentery = Entry(root,textvariable=adressvalue)
genderentery = Entry(root,textvariable=gendervalue)

nameentery.grid(row=1,column=3)
passwordentery.grid(row=2,column=3)
adressentery.grid(row=3,column=3)
genderentery.grid(row=4,column=3)

btn = Button(root,text="submit to aarv" ,command=getvals)
btn.grid(row=5,column=3)
root.mainloop()