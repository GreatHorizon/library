import tkinter as Tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime, date, time, timezone
import psycopg2

def RegisterStudent(id, firstName, lastName,  dateOfBirth, phone, email) :
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
    cursor = conn.cursor()
    date = datetime.strptime(dateOfBirth, "%Y-%m-%d").date()

    try:
        cursor.execute("INSERT INTO student(id_student, first_name, last_name, date_of_birth, phone_number, email)"
        + "VALUES (%s, %s, %s, %s, %s, %s)"
        , (id, firstName, lastName, date, phone, email))
        conn.commit()
        messagebox.showinfo('Success', "Student added successfully")
    except:
        messagebox.showinfo('Failed', "Data cant be written into db")


def MakeWindow() :
    root = Tk()
    root.title("library")
    root.minsize(width=900, height=400)
    root.geometry("900x500")

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx = -0, rely = 0, relwidth = 1, relheight = 1)

    lb1 = Label(labelFrame,text="Student ID", bg='black', fg='white')
    lb1.place(relx = 0.1, rely = 0.2, relheight = 0.08)

    lb2 = Label(labelFrame, text="First Name", bg='black', fg='white')
    lb2.place(relx = 0.1, rely = 0.3, relheight = 0.08)

    lb3 = Label(labelFrame, text="Last name", bg='black', fg='white')
    lb3.place(relx = 0.1, rely = 0.4, relheight = 0.08)

    lb4 = Label(labelFrame, text="Date of birth", bg='black', fg='white')
    lb4.place(relx = 0.1, rely = 0.5, relheight = 0.08)

    lb5 = Label(labelFrame, text="Phone", bg='black', fg='white')
    lb5.place(relx = 0.1, rely = 0.6, relheight = 0.08)

    lb6 = Label(labelFrame, text="Email", bg='black', fg='white')
    lb6.place(relx = 0.1, rely = 0.7, relheight = 0.08)

    studentIdField = Entry(labelFrame)
    studentIdField.place(relx = 0.2, rely = 0.2, relwidth = 0.3, relheight = 0.05)

    studentFirstNameField = Entry(labelFrame)
    studentFirstNameField.place(relx = 0.2, rely = 0.3, relwidth = 0.3, relheight = 0.05)

    studentLastNameField = Entry(labelFrame)
    studentLastNameField.place(relx = 0.2, rely = 0.4, relwidth = 0.3, relheight = 0.05)

    studentDateOfBirthField = Entry(labelFrame)
    studentDateOfBirthField.place(relx = 0.2, rely = 0.5, relwidth = 0.3, relheight = 0.05)

    studentPhoneField = Entry(labelFrame)
    studentPhoneField.place(relx = 0.2, rely = 0.6, relwidth = 0.3, relheight = 0.05)

    studentEmailField = Entry(labelFrame)
    studentEmailField.place(relx = 0.2, rely = 0.7, relwidth = 0.3, relheight = 0.05)

    SubmitBtn = Button(root,text="Register student",bg='#d1ccc0', fg='black',
    command=lambda:RegisterStudent(studentIdField.get(), studentFirstNameField.get(), studentLastNameField.get(),
    studentDateOfBirthField.get(), studentPhoneField.get(), studentEmailField.get()))

    SubmitBtn.place(relx=0.25,rely=0.7, relwidth=0.18,relheight=0.08)
    SubmitBtn.grid()

    root.mainloop()
