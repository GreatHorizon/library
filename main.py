import tkinter as tk
from tkinter import *
from datetime import datetime, date, time, timezone

from Views.RegisterNewUser import *
from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.StartPage import StartPage
from Views.AdminPage import AdminPage
from Views.RegisterStudentPage import RegisterStudentPage
from Views.AddBookPage import AddBookPage

from Models.AdminAutorizationModel import AdminAuthorizationModel
from Models.StartPageModel import StartPageModel
from Models.AdminPageModel import AdminPageModel
from Models.RegisterStudentModel import RegisterStudentModel
from Models.AddBookModel import AddBookModel

class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.container = tk.Frame(self)
        self.title("library")

        tk.Tk.geometry(self,'900x400') 
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.models = {
            StartPage: StartPageModel,
            AdminAuthorizationPage: AdminAuthorizationModel,
            AdminPage: AdminPageModel,
            RegisterStudentPage: RegisterStudentModel,
            AddBookPage: AddBookModel
        }

        self.frames = {}
        for F in (StartPage
                , AdminAuthorizationPage
                , AdminPage
                , RegisterStudentPage
                , AddBookPage):

            model = self.models[F]
            frame = F(self.container, self, model())

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = Window()
app.mainloop()