import tkinter as tk
from tkinter import *
from Controllers.EditInfoController import EditInfoController

class EditInfoPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master)
        self._model = model
        self._controller = EditInfoController(master, self._model, self)
        self._model.Register(self)

        label = tk.Label(self, text="Change your info")
        label.config(font=("Courier", 16))
        label.pack(pady=10, padx=10)

        nameLabel = Label(self,text="Name: Stas Gaisin", fg='black')
        nameLabel.place(relx = 0.45, rely = 0.12, relheight = 0.08)

        birthdayLabel = Label(self,text="Birthday: 30.11.2000", fg='black')
        birthdayLabel.place(relx = 0.45, rely = 0.18, relheight = 0.08)
        
        phoneLabel = Label(self,text="Phone: 89023333492", fg='black')
        phoneLabel.place(relx = 0.45, rely = 0.24, relheight = 0.08)

        emailLabel = Label(self,text="Email: stas@mail.ru", fg='black')
        emailLabel.place(relx = 0.45, rely = 0.30, relheight = 0.08)

        lb1 = Label(self,text="New email", fg='black')
        lb1.place(relx = 0.25, rely = 0.5, relheight = 0.08)

        self.newEmailField = Entry(self, width = 30)
        self.newEmailField.place(relx = 0.35, rely = 0.5, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="New phone", fg='black')
        lb2.place(relx = 0.25, rely = 0.65, relheight = 0.08)

        self.newPhoneField = Entry(self, width = 30)
        self.newPhoneField.place(relx = 0.35, rely = 0.65, relwidth = 0.3, relheight = 0.08)

        self.message = Label(self)
        self.message.place(relx = 0.35, rely = 0.75, relheight = 0.05)
        
        button = tk.Button(self, text="Sumbit",
            command=lambda:self._controller.ChangePassword(self.oldPassField.get(),
            self.newPassField.get(), self.confirmPassField.get()))
        button.place(relx=0.4, rely=0.80, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToStudentPage())
        button.place(relx = 0.35, rely = 0.80, relheight = 0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        pass