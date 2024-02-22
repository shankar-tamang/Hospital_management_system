import tkinter as tk

class Label_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.label1 = tk.Label(self.root, text="Hello World")
        self.label2 = tk.Label(self.root, text = "Hello Again")
        self.label1.pack()
        self.label2.pack()
        tk.mainloop()

gui = Label_GUI()