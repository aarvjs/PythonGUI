import tkinter as tk
from tkinter import ttk

class NewspaperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("This is my Third Project")
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Create title
        title_label = tk.Label(self.root, text="Daily News", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=10)

        # Create headlines section
        headlines_frame = ttk.LabelFrame(self.root, text="Headlines", padding=(10, 10))
        headlines_frame.pack(fill="x", padx=10, pady=5)

        headlines = ["Breaking News: Arvind learned Python Tkintert", 
                     "Sports: Local Team Wins Championship", 
                     "Weather: Sunny with a Chance of Showers"]

        for headline in headlines:
            headline_label = tk.Label(headlines_frame, text=headline, font=("Helvetica", 14))
            headline_label.pack(anchor="w", pady=2)

        # Create news content section
        content_frame = ttk.LabelFrame(self.root, text="News Content", padding=(10, 10))
        content_frame.pack(fill="both", expand=True, padx=10, pady=5)

        news_content = ("I have completed c programming, c++, html, css, javascript,bootstra. "
                        "Tailwind css, wordpress, python, django, tkinter, pyautogui. "
                        "php , mysql, mongoDB , reactjs , and make many project.")

        content_text = tk.Text(content_frame, wrap="word", font=("Helvetica", 12))
        content_text.insert("1.0", news_content)
        content_text.config(state="disabled")
        content_text.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewspaperApp(root)
    root.mainloop()
