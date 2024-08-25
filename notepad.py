
import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
    if file:
        text_area.delete(1.0, tk.END)
        text_area.insert(1.0, file.read())
        file.close()

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
    if file:
        file.write(text_area.get(1.0, tk.END))
        file.close()

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

def undo_action():
    text_area.event_generate(("<<Undo>>"))

def cut_action():
    text_area.event_generate(("<<Cut>>"))

def copy_action():
    text_area.event_generate(("<<Copy>>"))

def paste_action():
    text_area.event_generate(("<<Paste>>"))

def select_all_action():
    text_area.tag_add("sel", "1.0", "end")

font_size = 12  

# zoom 

def zoom_in(event=None):
    global font_size
    font_size += 2
    text_area.config(font=("Arial", font_size))

def zoom_out(event=None):  
    global font_size
    if font_size > 6: 
        font_size -= 2
    text_area.config(font=("Arial", font_size))

def reset_zoom():
    global font_size
    font_size = 12  
    text_area.config(font=("Arial", font_size))

# Dark mode Light mode
def toggle_dark_mode():
    text_area.config(bg="black", fg="white", insertbackground="white")

def toggle_light_mode():
    text_area.config(bg="white", fg="black", insertbackground="black")

root = tk.Tk()
root.title("My first project")
root.geometry("600x400")

text_area = tk.Text(root, font=("Arial", 12), undo=True)
text_area.pack(expand=True, fill='both')

menu_bar = tk.Menu(root)

m1 = tk.Menu(menu_bar, tearoff=0)
m1.add_command(label="New", command=new_file)
m1.add_command(label="Open", command=open_file)
m1.add_command(label="Save", command=save_file)
m1.add_separator()
m1.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=m1)

m2 = tk.Menu(menu_bar, tearoff=0)
m2.add_command(label="Undo", command=undo_action)
m2.add_separator()
m2.add_command(label="Cut", command=cut_action)
m2.add_command(label="Copy", command=copy_action)
m2.add_command(label="Paste", command=paste_action)
m2.add_separator()
m2.add_command(label="Select All", command=select_all_action)
menu_bar.add_cascade(label="Edit", menu=m2)

m3 = tk.Menu(menu_bar, tearoff=0)
m3.add_command(label="Zoom In", command=zoom_in)
m3.add_command(label="Zoom Out", command=zoom_out)
m3.add_command(label="Reset Zoom", command=reset_zoom)
menu_bar.add_cascade(label="View", menu=m3)


m4 = tk.Menu(menu_bar, tearoff=0)
m4.add_command(label="Dark Mode", command=toggle_dark_mode)
m4.add_command(label="Light Mode", command=toggle_light_mode)
menu_bar.add_cascade(label="Theme", menu=m4)

root.config(menu=menu_bar)


root.bind("<Control-Key-=>", zoom_in)  # Ctrl + = for Zoom In
root.bind("<Control-Key-minus>", zoom_out)  # Ctrl + - for Zoom Out

root.mainloop()
