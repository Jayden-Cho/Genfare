import customtkinter as ctk
from PIL import ImageTk
import tkinter as tk
from glob import glob
import os

# Selecting GUI theme - dark, light , system (for system default)
#ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
#ctk.set_default_color_theme("blue")

app = tk.Tk()
width, height = 800, 600
width_screen, height_screen = app.winfo_screenwidth(), app.winfo_screenheight()
x, y = (width_screen/2) - (width/2), (height_screen/2) - (height/2)
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.title("Farebox Configuration Assistant")
app.iconphoto(False, ImageTk.PhotoImage(file='spx.png'))
#app.resizable(False, False)

title = tk.Label(master=app, text="Configuration Assistant", font=("Arial", 40))
title.place(x=50, y=100)


start = tk.Frame(master=app, width=700, height=150)
start.place(x=50, y=210)

label_start = tk.Label(master=start,
                           text="Start",
                           font=("Arial", 20))
label_start.pack(side='left')
label_start.place(x=0, y=0)

button_new_project = tk.Button(master=start, text="New Project", font=("Arial", 15), height=-1, anchor='w')
button_load_project = tk.Button(master=start, text="Load Project", font=("Arial", 15), height=-1, anchor='w')

button_new_project.place(x=0, y=30)
button_load_project.place(x=0, y=55)


recent = tk.Frame(master=app, width=700, height=150)
recent.place(x=50, y=370)

label_recent = tk.Label(master=recent, text="Recent", font=("Arial", 20))
label_recent.place(x=0, y=0)

flist = glob('*.py')
flist.sort(key=os.path.getmtime, reverse=True)

listbox_recent = tk.Listbox(master=recent)
listbox_recent.place(x=0, y=25)

num_to_show = min(len(flist), 5)
for i in range(num_to_show):
    listbox_recent.insert(tk.END, flist[i])

app.mainloop()  