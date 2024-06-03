import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox

filename = None


def new_file():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)


def save_file():
    global filename
    if not filename:
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:  # Proceed only if a file name is specified
        try:
            t = text.get(0.0, tk.END)
            with open(filename, 'w') as f:
                f.write(t)
        except Exception as e:
            messagebox.showerror(title='Oops!', message=f'Unable to save file: {e}')
    else:
        messagebox.showinfo(title='Save Cancelled', message='Save operation was cancelled.')


def save_as():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title='Oops!', message='Unable to save file')


def open_file():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


root = Tk()
root.title('Cipher Text Editor')
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = Text(root, width=500, height=500)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=new_file)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_file)
filemenu.add_command(label='Save As', command=save_as)
filemenu.add_separator()
filemenu.add_command(label='uit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

root.config(menu=menubar)
root.mainloop()
