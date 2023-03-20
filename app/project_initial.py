import customtkinter as ctk
from PIL import ImageTk
import tkinter as tk
from glob import glob
import os

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

app = ctk.CTk()
width, height = 800, 600
width_screen, height_screen = app.winfo_screenwidth(), app.winfo_screenheight()
x, y = (width_screen/2) - (width/2), (height_screen/2) - (height/2)
app.geometry('%dx%d+%d+%d' % (width, height, x, y))
app.title("Farebox Configuration Assistant")
app.iconphoto(False, ImageTk.PhotoImage(file='spx.png'))
#app.resizable(False, False)

title = ctk.CTkLabel(master=app, text="Configuration Assistant", font=("Arial", 40))
title.place(x=50, y=100)


start = ctk.CTkFrame(master=app, width=700, height=150, fg_color="transparent")
start.place(x=50, y=210)

label_start = ctk.CTkLabel(master=start,
                           text="Start",
                           fg_color="transparent",
                           font=("Arial", 20))
label_start.pack(side='left')
label_start.place(x=0, y=0)

button_new_project = ctk.CTkButton(master=start, text="New Project", font=("Arial", 15), fg_color="transparent", height=-1, anchor='w', hover=False)
button_load_project = ctk.CTkButton(master=start, text="Load Project", font=("Arial", 15), fg_color="transparent", height=-1, anchor='w', hover=False)

button_new_project.place(x=0, y=30)
button_load_project.place(x=0, y=55)


recent = ctk.CTkFrame(master=app, width=700, height=150, fg_color="transparent")
recent.place(x=50, y=370)

label_recent = ctk.CTkLabel(master=recent, text="Recent", fg_color="transparent", font=("Arial", 20))
label_recent.place(x=0, y=0)

flist = glob('*.py')
flist.sort(key=os.path.getmtime, reverse=True)

listbox_recent = tk.Listbox(master=recent)
listbox_recent.place(x=0, y=25)

num_to_show = min(len(flist), 5)
for i in range(num_to_show):
    listbox_recent.insert(tk.END, flist[i])

app.mainloop()  