import tkinter as tk
from tkinter import *
from Controllers.RegisterStudentController import RegisterStudentController
from tkcalendar import *
  

class RegisterStudentPage(tk.Frame):
    def __init__(self, master, model):
        tk.Frame.__init__(self, master) 
        self._model = model
        self._controller = RegisterStudentController(master, self._model, self)
        self._model.Register(self)


        label = tk.Label(self, text="Page for librarian with new student registration")
        label.config(font=("Courier", 12))
        label.pack(pady=10,padx=10)

        lb1 = Label(self,text="Student ID", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        lb2 = Label(self, text="First Name", fg='black')
        lb2.place(relx = 0.25, rely = 0.25, relheight = 0.08)

        lb3 = Label(self, text="Last name", fg='black')
        lb3.place(relx = 0.25, rely = 0.35, relheight = 0.08)

        lb4 = Label(self, text="Date of birth", fg='black')
        lb4.place(relx = 0.25, rely = 0.45, relheight = 0.08)

        lb5 = Label(self, text="Phone", fg='black')
        lb5.place(relx = 0.25, rely = 0.55, relheight = 0.08)

        lb6 = Label(self, text="Email", fg='black')
        lb6.place(relx = 0.25, rely = 0.65, relheight = 0.08)

        self.studentIdField = Entry(self)
        self.studentIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.05)

        self.studentFirstNameField = Entry(self)
        self.studentFirstNameField.place(relx = 0.35, rely = 0.25, relwidth = 0.3, relheight = 0.05)

        self.studentLastNameField = Entry(self)
        self.studentLastNameField.place(relx = 0.35, rely = 0.35, relwidth = 0.3, relheight = 0.05)
        
        self.birthdayField = DateEntry(self, date_pattern='dd-mm-y')
        self.birthdayField.drop_down()
        self.birthdayField.focus()
        self.birthdayField.place(relx = 0.35, rely = 0.45, relwidth = 0.3, relheight = 0.05)

        self.studentPhoneField = Entry(self)
        self.studentPhoneField.place(relx = 0.35, rely = 0.55, relwidth = 0.3, relheight = 0.05)

        self.studentEmailField = Entry(self)
        self.studentEmailField.place(relx = 0.35, rely = 0.65, relwidth = 0.3, relheight = 0.05)


        self.message = Label(self)
        self.message.place(relx = 0.35, rely = 0.72, relheight = 0.05)
        
        SubmitBtn = Button(self, text="Register student", fg='black',
        command=lambda:self._controller.RegisterStudent(self.studentIdField.get(), self.studentFirstNameField.get(), self.studentLastNameField.get(),
        self.birthdayField.get(), self.studentPhoneField.get(), self.studentEmailField.get()))
        SubmitBtn.place(relx=0.4, rely=0.8, relwidth=0.25,relheight=0.1)

        button = tk.Button(self, text="<<",
        command=lambda:self._controller.BackToAdminPage())
        button.place(relx = 0.35, rely = 0.8, relheight = 0.1)

    def Notify(self):
        if(self._model._isRegistrated):
            self.ClearFields()
            self.message.config(text=self._model._message, fg='green')
        else:
            self.message.config(text=self._model._message, fg='red')
        

    def ClearFields(self):
        self.studentIdField.delete(0, len(self.studentIdField.get()))
        self.studentEmailField.delete(0, len(self.studentEmailField.get()))
        self.studentPhoneField.delete(0, len(self.studentPhoneField.get()))
        self.studentFirstNameField.delete(0, len(self.studentFirstNameField.get()))
        self.studentLastNameField.delete(0, len(self.studentLastNameField.get()))

    def ClearMessageLabel(self):
        self.message.config(text='')
