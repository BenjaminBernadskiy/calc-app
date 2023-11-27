import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

menu_frame = tk.Frame(root)
menu_frame.pack(fill="x")

text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)

menu = tk.Menu(menu_frame)

def new_note():
    pass

new_icon = tk.PhotoImage(file="new.png")
open_icon = tk.PhotoImage(file="open.png")
close_icon = tk.PhotoImage(file="close.png")
save_icon = tk.PhotoImage(file="save.png")

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New",image=new_icon, compound=tk.LEFT, command=new_note)

root.config(menu=menu)

text_area = ScrolledText(text_frame, wrap=tk.WORD)
text_area.pack(fill="both")

root.mainloop()