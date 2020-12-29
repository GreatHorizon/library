import tkinter as tk
from tkinter import *

from Controllers.AddBookController import AddBookController

class AddBookPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = AddBookController(master, self._model, self)
        self._model.Register(self)

        lb1 = Label(self,text="Book name", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        lb2 = Label(self, text="Author", fg='black')
        lb2.place(relx = 0.25, rely = 0.25, relheight = 0.08)

        lb3 = Label(self, text="Page count", fg='black')
        lb3.place(relx = 0.25, rely = 0.35, relheight = 0.08)

        lb4 = Label(self, text="ISBN", fg='black')
        lb4.place(relx = 0.25, rely = 0.45, relheight = 0.08)

        lb5 = Label(self, text="Publisher", fg='black')
        lb5.place(relx = 0.25, rely = 0.55, relheight = 0.08)


        self.bookNameField = Entry(self)
        self.bookNameField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.05)

        self.authorNameField = Entry(self)
        self.authorNameField.place(relx = 0.35, rely = 0.25, relwidth = 0.3, relheight = 0.05)

        self.pageCountField = Entry(self)
        self.pageCountField.place(relx = 0.35, rely = 0.35, relwidth = 0.3, relheight = 0.05)

        self.bookIdField = Entry(self)
        self.bookIdField.place(relx = 0.35, rely = 0.45, relwidth = 0.3, relheight = 0.05)

        self.publisherField = Entry(self)
        self.publisherField.place(relx = 0.35, rely = 0.55, relwidth = 0.3, relheight = 0.05)

        self.message = Label(self, text='', fg='red')
        self.message.place(relx = 0.35, rely = 0.60, relheight = 0.05)

        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToAdminPage())
        button.place(relx=0.4, rely=0.85, relwidth=0.2,relheight=0.1)

        SubmitBtn = Button(self, text="Add book",bg='#d1ccc0', fg='black',
        command=lambda:self._controller.AddBook(self.bookIdField.get(), self.bookNameField.get(),
        self.authorNameField.get(), self.pageCountField.get(), self.publisherField.get()))
        SubmitBtn.place(relx=0.4, rely=0.75, relwidth=0.2,relheight=0.1)

    def Notify(self):
        if self._model._addedSuccessfuly:
            self.message.config(text=self._model._description, fg='green')
        else:
            self.message.config(text=self._model._description, fg='red')