import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import psycopg2
# from Database.database import *
from Controllers.StudentIssuancePageController import StudentIssuancePageController

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class StudentIssuancePage(tk.Frame):

    def __init__(self, parent, window, model):
        tk.Frame.__init__(self, parent)
        self._model = model
        self._controller = StudentIssuancePageController(window, self._model, self)
        self._model.Register(self)
        

        
        issuanceList = self._controller.GetStudentIssuance(1180501039)
        print(issuanceList)
        labelFrame = Frame(self,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

        Label(labelFrame, text="%-30s%-60s%-50s%-50s"%('Book ID','Title','Author','Deadline'),bg='black',fg='white').place(relx=0.07,rely=0.05)
        Label(labelFrame, text="--------------------------------------------------------------------------------------------------------------------------------",
        bg='black',fg='white').place(relx=0.05,rely=0.2)

        y = 0.3
        for issuance in issuanceList:
            Label(labelFrame, text="%-30s%-50s%-50s%-50s"%(issuance[0], issuance[1], issuance[2], issuance[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1

        # self._controller.GetStudentIssuance(1)

        button = tk.Button(self, text="<<",
                            command=lambda:self._controller.BackToStudentPage())
        button.place(relx = 0.35, rely = 0.80, relheight = 0.1)

        button = tk.Button(self, text="Sumbit",
            command=lambda:self._controller.GetStudentIssuance(self.id))
        button.place(relx=0.4, rely=0.80, relwidth=0.25, relheight=0.1)


        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("11111111111", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.3)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.4)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.5)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.6)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.7)
        #         Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.4)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.5)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.6)
        # Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=0.7)

        # y = 0.3
        # for i in range(20) :
        #     Label(labelFrame, text="%-10s%-30s%-30s%-20s"%("asdasd", "asdasd", "asdasd", "asdasd"),bg='black',fg='white').place(relx=0.07,rely=y)
        #     y += 0.1

            






    # def Notify(self):
    #     if (self._model._isAuthorizated):
    #         self._controller.SendData(id=self._model._userId)
    #         self._controller.OpenStudentPage()
    #         self.ClearErrorLabel()
    #     else:
    #         self.error.config(text=self._model._message)
    #     self.ClearFields()

    # def ClearFields(self):
    #     self.studentIdField.delete(0, len(self.studentIdField.get()))
    #     self.passwordField.delete(0, len(self.passwordField.get()))

    # def ClearErrorLabel(self):
    #     self.error.config(text='') 

    def updateView(self) :
        self._controller.GetStudentIssuance(self.id)

    def recieve_data(self, **data):
        self.id = data['id']
