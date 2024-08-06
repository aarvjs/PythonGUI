import tkinter as tk
import math
import random

class FlowerWaveLoader:
    def __init__(self, root):
        self.root = root
        self.root.title("Flower Wave Loader with DJ Lights")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='black', highlightthickness=0)
        self.canvas.pack()
        
        self.arc_radius = 100
        self.line_width = 10
        self.num_arcs = 8
        self.arc_length = 45
        self.angle_shift = 0
        self.colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'orange', 'purple']
        
        self.arcs = [
            self.canvas.create_arc(
                200 - self.arc_radius, 200 - self.arc_radius, 
                200 + self.arc_radius, 200 + self.arc_radius,
                start=45 * i, extent=self.arc_length, 
                style=tk.ARC, outline=self.colors[i % len(self.colors)], 
                width=self.line_width
            ) for i in range(self.num_arcs)
        ]
        
        self.update_loader()

    def update_loader(self):
        self.angle_shift = (self.angle_shift + 5) % 360
        for i, arc in enumerate(self.arcs):
            start_angle = (45 * i + self.angle_shift) % 360
            self.canvas.itemconfig(arc, start=start_angle)
            # Update color to simulate DJ light effect
            color = random.choice(self.colors)
            self.canvas.itemconfig(arc, outline=color)
        
        self.root.after(30, self.update_loader)

if __name__ == "__main__":
    root = tk.Tk()
    loader = FlowerWaveLoader(root)
    root.mainloop()
# import tkinter as tk
# from tkinter import scrolledtext

# # Function to simulate command execution
# def execute_command():
#     command = command_entry.get()
#     output = f"> {command}\nExecuting command...\nCommand '{command}' executed successfully.\n"
#     output_area.insert(tk.END, output)
#     command_entry.delete(0, tk.END)

# # Create the main window
# root = tk.Tk()
# root.title(" this is my second Project. Hacker Tool")
# root.geometry("800x600")
# root.configure(bg="black")

# # Create a scrolled text area for displaying output
# output_area = scrolledtext.ScrolledText(root, bg="black", fg="green", font=("Courier", 12))
# output_area.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)
# output_area.insert(tk.END, "Hacker Tool  - Enter your commands below:\n")
# output_area.config(state=tk.DISABLED)

# # Create an entry widget for command input
# command_entry = tk.Entry(root, bg="black", fg="green", font=("Courier", 12))
# command_entry.pack(pady=10, padx=10, fill=tk.X)

# # Create a button to execute the command
# execute_button = tk.Button(root, text="Execute", command=execute_command, bg="green", fg="black", font=("Courier", 12))
# execute_button.pack(pady=10, padx=10)

# # Run the Tkinter event loop
# root.mainloop()
