import tkinter as tk
from tkinter import *
import utils as U
from PIL import ImageTk
import customtkinter as ctk
import tkinter.messagebox as tkmb

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        login_setup()
        # Setup initial screen
        self.title("Genfare Configuration Assistant")
        self.geometry("720x550")
        self.resizable(True, True)
        self.iconphoto(False, tk.PhotoImage(file="spx.png"))
    
        # create a container
        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        # Initialize Frames
        self.frames = {}
        self.HomePage = HomePage
        self.Validation = Validation

        # Defining Frames
        for F in {HomePage, Validation}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")    
           
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        # put the frame on front
        frame.tkraise()
 

def login_setup():
    # Selecting GUI theme - dark, light , system (for system default)
    ctk.set_appearance_mode("dark")
    
    # Selecting color theme - blue, green, dark-blue
    ctk.set_default_color_theme("blue")
    
    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Farebox Configuration Assistant")
    
    
    def login():
    
        username = "genfare"
        password = "fastfare"
    
        if user_entry.get() == username and user_pass.get() == password:
            tkmb.showinfo(title="Login Successful",message="You have logged in successfully")
            frame.quit()
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

class HomePage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Welcome to the Genfare Configuration Assistant", font=('Times', '20'))
        label.pack(pady=0,padx=0)

        new_project = tk.Button(self, text="Create new project", font=('Times', '10'))
        new_project.place(x=20, y=100)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        # proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        # help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar

class Validation(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Validation Page", font=('Times', '20'))
        label.pack(pady=0,padx=0)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=3, relief=RAISED, activebackground="#80B9DC")

        # Filemenu
        filemenu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project", command=lambda: parent.show_frame(parent.Validation))
        filemenu.add_command(label="Close", command=lambda: parent.show_frame(parent.HomePage))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)  

        # proccessing menu
        processing_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Validation", menu=processing_menu)
        processing_menu.add_command(label="validate")
        processing_menu.add_separator()

        # help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=U.about)
        help_menu.add_separator()

        return menubar


if __name__ == "__main__":

    app = App()
    app.mainloop()
