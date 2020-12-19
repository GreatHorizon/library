import tkinter as tk
from tkinter import *
from datetime import datetime, date, time, timezone

from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.StartPage import StartPage
from Views.AdminPage import AdminPage
from Views.RegisterStudentPage import RegisterStudentPage
from Views.AddBookPage import AddBookPage
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.StudentPage import StudentPage
from Views.ChangeStudentPasswordPage import ChangeStudentPasswordPage
from Views.BookIssuePage import BookIssuePage

from Models.AdminAutorizationModel import AdminAuthorizationModel
from Models.StartPageModel import StartPageModel
from Models.AdminPageModel import AdminPageModel
from Models.RegisterStudentModel import RegisterStudentModel
from Models.AddBookModel import AddBookModel
from Models.StudentAuthorizationModel import StudentAuthorizationModel
from Models.StudentPageModel import StudentPageModel
from Models.ChangeStudentPasswordModel import ChangeStudentPasswordModel
from Models.BookIssueModel import BookIssueModel


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
            AddBookPage: AddBookModel,
            StudentAuthorizationPage : StudentAuthorizationModel,
            RegisterStudentPage: RegisterStudentModel,
            StudentPage: StudentPageModel,
            ChangeStudentPasswordPage: ChangeStudentPasswordModel,
            BookIssuePage: BookIssueModel
        }

        self.frames = {}
        for F in (StartPage
                , AdminAuthorizationPage
                , AdminPage
                , RegisterStudentPage
                , AddBookPage
                , StudentAuthorizationPage
                , StudentPage
                , ChangeStudentPasswordPage
                , BookIssuePage
                ):

            model = self.models[F]
            frame = F(self.container, self, model())

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def send_data(self, page, **data):
        frame = self.frames[page]
        frame.recieve_data(**data)


app = Window()
app.mainloop()