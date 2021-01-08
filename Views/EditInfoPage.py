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

        studentInfo = self._controller.GetStudentInfo()

        self.nameLabel = Label(self,text="", fg='black')
        self.nameLabel.config(font=("Courier", 10))
        self.nameLabel.place(relx = 0.4, rely = 0.12, relheight = 0.08)

        self.birthdayLabel = Label(self,text="", fg='black')
        self.birthdayLabel.config(font=("Courier", 10))
        self.birthdayLabel.place(relx = 0.4, rely = 0.18, relheight = 0.08)
        
        self.phoneLabel = Label(self,text="", fg='black')
        self.phoneLabel.config(font=("Courier", 10))
        self.phoneLabel.place(relx = 0.4, rely = 0.24, relheight = 0.08)

        self.emailLabel = Label(self,text="", fg='black')
        self.emailLabel.config(font=("Courier", 10))
        self.emailLabel.place(relx = 0.4, rely = 0.30, relheight = 0.08)

        self.ShowStudentInfo(studentInfo)

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
            command=lambda:self._controller.ChangeInfo(self.newEmailField.get(),
            self.newPhoneField.get()))
        button.place(relx=0.4, rely=0.80, relwidth=0.25, relheight=0.1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToStudentPage())
        button.place(relx = 0.35, rely = 0.80, relheight = 0.1)

    def SetMessageLabel(self, message, color):
        self.message.config(text=message, fg=color)

    def Notify(self):
        pass

    def ShowStudentInfo(self, studentInfo):
        self.nameLabel.config(text='Name: ' + studentInfo[0] + ' ' + studentInfo[1])
        self.birthdayLabel.config(text='Birthday: ' + str(studentInfo[2]))
        self.emailLabel.config(text='Email: ' + studentInfo[3])
        self.phoneLabel.config(text='Phone: ' + studentInfo[4])