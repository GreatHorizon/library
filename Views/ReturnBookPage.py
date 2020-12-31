import tkinter as tk
from tkinter import *
from Controllers.ReturnBookController import ReturnBookController


class ReturnBookPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self,master)
        self._model = model
        self._controller = ReturnBookController(master, self._model, self)

        
        lb1 = Label(self,text="Book id", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        self.copyIdField = Entry(self, width = 30)
        self.copyIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)
    
        self.message = Label(self, text='', fg='red')
        self.message.place(relx = 0.35, rely = 0.30, relheight = 0.05)

        button = tk.Button(self, text="Sumbit",
            command=lambda:self._controller.ReturnBook(self.copyIdField.get()))
        button.place(relx=0.4, rely=0.35, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.35, relheight = 0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        if (self._model._isDeleted):
            self.ClearFields()
            self.SetMessageLabel(self._model._message, 'green')
        else:
            self.SetMessageLabel(self._model._message, 'red')

    def ClearFields(self):
        self.copyIdField.delete(0, len(self.copyIdField.get()))
    
    def ClearMessageLabel(self):
        self.message.config(text='')

    # def recieve_data(self, **data):
    #     self.id = data['id']