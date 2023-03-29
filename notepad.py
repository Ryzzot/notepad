from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

current_file = None

def new_file():
    global current_file
    text.delete("1.0", END)
    current_file = None

def save_file():
    global current_file
    if not current_file:
        current_file = asksaveasfilename(defaultextension=".txt",
                                          filetypes=[("Text Files", "*.txt"),
                                                     ("All Files", "*.*")])
        if not current_file:
            return
    with open(current_file, "w") as f:
        f.write(text.get("1.0", END))

def open_file():
    global current_file
    file_path = askopenfilename(defaultextension=".txt",
                                filetypes=[("Text Files", "*.txt"),
                                           ("All Files", "*.*")])
    if not file_path:
        return
    text.delete("1.0", END)
    with open(file_path, "r") as f:
        text.insert(END, f.read())
    current_file = file_path

# create the root window
root = Tk()
root.title("Simple Notepad")

# create the text area
text = Text(root, font=("Helvetica", 12))
text.pack(expand=True, fill=BOTH)

# create the menu bar
menu_bar = Menu(root)

# create the file menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# add the menu bar to the root window
root.config(menu=menu_bar)

# start the main loop
root.mainloop()
