import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import ImageTk
import tkinter as tk
  
  
# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("dark")
  
# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")
  
app = ctk.CTk()
app.geometry("400x400")
app.title("Farebox Configuration Assistant")
# icon = tk.PhotoImage(file='spx.png')
# app.iconphoto(True, icon)
app.iconphoto(False, ImageTk.PhotoImage(file='spx.png'))
  
  
def login():
  
    username = "genfare"
    password = "fastfare"
  
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password',message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username',message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed",message="Invalid Username and password")
  
  
  
label = ctk.CTkLabel(app,
                     text="Welcome to the Farebox Configuration Assistant",
                     font = ("Arial", 15))
  
label.pack(pady=20)
  
  
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)
  
label = ctk.CTkLabel(master=frame,text='Enter Username and Password')
label.pack(pady=12,padx=10)
  
  
user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)
  
  
button = ctk.CTkButton(master=frame,text='Login',command=login)
button.pack(pady=12,padx=10)
  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)
  
  
app.mainloop()