import tkinter as tk


root = tk.Tk() # declaring the window
root.geometry("800x500") # setting the dimension of the window
root.title("My First GUI")  # setting the title of the window

label = tk.Label(root, text="Hello World!", font=('Arial', 18)) 
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height= 3, font=('Arial',16)) # height 3 means 3 line
textbox.pack(padx=20) 

# myentry = tk.Entry(root)  # entry is great for one line textbox
# myentry.pack()

button = tk.Button(root, text="Click Me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop() 