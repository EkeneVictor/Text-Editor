import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox

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
    except Exception as e:
        messagebox.showerror(title='Oops!', message=f'Unable to save file: {e}')


def open_file():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


def undo_text():
    try:
        text.edit_undo()
    except tk.TclError:
        pass


def redo_text():
    try:
        text.edit_redo()
    except tk.TclError:
        pass


def cut_text(event=None):
    text.event_generate("<<Cut>>")


def copy_text(event=None):
    text.event_generate("<<Copy>>")


def paste_text(event=None):
    text.event_generate("<<Paste>>")


def delete_text(event=None):
    if text.tag_ranges("sel"):
        text.delete("sel.first", "sel.last")


def select_all_text(event=None):
    text.tag_add('sel', '1.0', 'end')


root = Tk()
root.title('Cipher Text Editor')
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = Text(root, width=500, height=500, undo=True)  # Enable undo functionality
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=new_file)
filemenu.add_command(label='Open', command=open_file)
filemenu.add_command(label='Save', command=save_file)
filemenu.add_command(label='Save As', command=save_as)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='Undo (Ctrl + Z)', command=undo_text)
editmenu.add_command(label='Redo (Ctrl + Y)', command=redo_text)
editmenu.add_separator()
editmenu.add_command(label='Cut', command=cut_text)
editmenu.add_command(label='Copy', command=copy_text)
editmenu.add_command(label='Paste', command=paste_text)
editmenu.add_command(label='Delete', command=delete_text)
editmenu.add_command(label='Select All', command=select_all_text)
menubar.add_cascade(label='Edit', menu=editmenu)

root.config(menu=menubar)
root.mainloop()
