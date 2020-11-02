import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime, date, time, timezone
from registerNewUser import *
import psycopg2

class Window(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("library")

        tk.Tk.geometry(self,'900x400') 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, NewStudentRegistrationPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):

    def FindUser(self, studentId) :
        connection = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student WHERE id_student = ' + studentId)
        if cursor.rowcount == 1:
            messagebox.showinfo("Hi", [row[1] for row in cursor])
        else :
            messagebox.showinfo("Fail", "Incorrect user id")
            
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10,padx=10)


        lb1 = Label(self,text="Student ID", fg='black')
        lb1.place(relx = 0.25, rely = 0.15, relheight = 0.08)

        studentIdField = Entry(self, width = 30)
        studentIdField.place(relx = 0.35, rely = 0.15, relwidth = 0.3, relheight = 0.08)

        lb2 = Label(self,text="Password", fg='black')
        lb2.place(relx = 0.25, rely = 0.25, relheight = 0.08)

        passwordField = Entry(self, width = 30)
        passwordField.place(relx = 0.35, rely = 0.25, relwidth = 0.3, relheight = 0.08)

        button = tk.Button(self, text="Go to page with student registration",
                            command=lambda: self.SignInStudent(studentIdField.get(), passwordField.get(), controller))
        
        button.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1)

    def SignInStudent(self, id, password, controller) :
        if ((id == "admin") and (password == "admin3355")):
            controller.show_frame(NewStudentRegistrationPage)
        else:
            self.FindUser(id)

class NewStudentRegistrationPage(tk.Frame):

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

app = Window()
app.mainloop()