import tkinter as tk
from tkinter import *
from Controllers.ChangeStudentPasswordController import ChangeStudentPasswordController

class ChangeStudentPasswordPage(tk.Frame):
    def __init__(self, parent, window, model):
        tk.Frame.__init__(self, parent)
        self._model = model
        self._controller = ChangeStudentPasswordController(window, self._model, self)
        self._model.Register(self)

        label = tk.Label(self, text="Change student password")
        label.pack(pady=10, padx=10)


        lb1 = Label(self,text="Old password", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        self.oldPassField = Entry(self, width = 30, show='*')
        self.oldPassField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="New password", fg='black')
        lb2.place(relx = 0.25, rely = 0.3, relheight = 0.08)

        self.newPassField = Entry(self, width = 30, show='*')
        self.newPassField.place(relx = 0.35, rely = 0.3, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="Confirm new password", fg='black')
        lb2.place(relx = 0.2, rely = 0.45, relheight = 0.08)

        self.confirmPassField = Entry(self, width = 30, show='*')
        self.confirmPassField.place(relx = 0.35, rely = 0.45, relwidth = 0.3, relheight = 0.08)

        self.message = Label(self)
        self.message.place(relx = 0.35, rely = 0.54, relheight = 0.05)
        
        button = tk.Button(self, text="Sumbit",
            command=lambda:self._controller.ChangePassword(self.id, self.oldPassField.get(),
            self.newPassField.get(), self.confirmPassField.get()))
        button.place(relx=0.4, rely=0.6, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToStudentPage())
        button.place(relx = 0.35, rely = 0.6, relheight = 0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        if (self._model._isChanged):
            self.ClearFields()
            self.SetMessageLabel(self._model._message, 'green')
        else:
            self.SetMessageLabel(self._model._message, 'red')

    def ClearFields(self):
        self.oldPassField.delete(0, len(self.oldPassField.get()))
        self.newPassField.delete(0, len(self.newPassField.get()))
        self.confirmPassField.delete(0, len(self.confirmPassField.get()))
    
    def ClearMessageLabel(self):
        self.message.config(text='')

    def recieve_data(self, **data):
        self.id = data['id']


