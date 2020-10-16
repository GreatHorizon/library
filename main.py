import numpy
import tkinter as Tk
from tkinter import *
import psycopg2

def addBook() :
    return

def SignInUser() :
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM book')
    
    for row in cursor:
        print(row)
    print("successfully connected") 

    conn.commit()       
    cursor.close()
    conn.close()          
    return

def MakeWindow() :
    root = Tk()
    root.title("library")
    root.minsize(width=900, height=400)
    root.geometry("900x500")

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx = -0, rely = 0, relwidth = 1, relheight = 1)

    lb1 = Label(labelFrame,text="Student ID", bg='black', fg='white')
    lb1.place(relx = 0.1, rely = 0.2, relheight = 0.08)

    studentIdField = Entry(labelFrame)
    studentIdField.place(relx = 0.2, rely = 0.2, relwidth = 0.3, relheight = 0.05)

    lb1 = Label(labelFrame, text="Password", bg='black', fg='white')
    lb1.place(relx = 0.1, rely = 0.3, relheight = 0.08)

    studentPasswordField = Entry(labelFrame)
    studentPasswordField.place(relx = 0.2, rely = 0.3, relwidth = 0.3, relheight = 0.05)

    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=SignInUser)
    SubmitBtn.place(relx=0.25,rely=0.4, relwidth=0.18,relheight=0.08)

    root.mainloop()

if __name__ == '__main__':
    MakeWindow()

