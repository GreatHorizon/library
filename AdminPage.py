import tkinter as tk
from tkinter import *

class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page for librarian with new student registration")
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

        studentIdField = Entry(self)
        studentIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.05)

        studentFirstNameField = Entry(self)
        studentFirstNameField.place(relx = 0.35, rely = 0.25, relwidth = 0.3, relheight = 0.05)

        studentLastNameField = Entry(self)
        studentLastNameField.place(relx = 0.35, rely = 0.35, relwidth = 0.3, relheight = 0.05)

        studentDateOfBirthField = Entry(self)
        studentDateOfBirthField.place(relx = 0.35, rely = 0.45, relwidth = 0.3, relheight = 0.05)

        studentPhoneField = Entry(self)
        studentPhoneField.place(relx = 0.35, rely = 0.55, relwidth = 0.3, relheight = 0.05)

        studentEmailField = Entry(self)
        studentEmailField.place(relx = 0.35, rely = 0.65, relwidth = 0.3, relheight = 0.05)

        SubmitBtn = Button(self, text="Register student",bg='#d1ccc0', fg='black',
        command=lambda:RegisterStudent(studentIdField.get(), studentFirstNameField.get(), studentLastNameField.get(),
        studentDateOfBirthField.get(), studentPhoneField.get(), studentEmailField.get()))
        SubmitBtn.place(relx=0.4, rely=0.75, relwidth=0.2,relheight=0.1)

        from StartPage import StartPage
        button = tk.Button(self, text="<<",
        command=lambda: controller.show_frame())
        button.place(relx=0.4, rely=0.85, relwidth=0.2,relheight=0.1)