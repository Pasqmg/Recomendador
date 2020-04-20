from datamanager.DataLoader import DataLoader
from tkinter import *


class NewUserPage(Frame):

    def __init__(self, parent, controller):
        db = DataLoader()
        db.read_all_data()

        Frame.__init__(self, parent)

        controller.geometry("500x500")

        title_Label = Label(self, text="Register a new user", width=20, font=("bold",20))
        title_Label.place(x=90,y=53)

        name_Label = Label(self, text="Username", width=20, font=("bold", 10))
        name_Label.place(x=80, y=130)
        name_Label.grid(row=1, column=0, pady=130, padx=25)

        name_Entry = Entry(self)
        name_Entry.place(x=240, y=130)
        name_Entry.grid(row=1, column=1)

        gender_Label = Label(self, text="Gender", width=20, font=("bold", 10))
        gender_Label.place(x=70, y=180)
        gender_Label.grid(row=2, column=0)
        var = IntVar()
        Radiobutton(self, text="Male", padx=5, variable=var, value=1).place(x=235,y=180)
        Radiobutton(self, text="Female", padx=20, variable=var, value=2).place(x=290, y=180)

        occupation_Label = Label(self, text="Occupation", width=20, font=("bold", 10))
        occupation_Label.place(x=70, y=230)
        occupation_list = db.get_occupation_list()
        print(occupation_list)
        c = StringVar()
        occupation_OptionMenu = OptionMenu(self, c, *occupation_list)
        occupation_OptionMenu.config(width=20)
        c.set("Select your occupation")
        occupation_OptionMenu.place(x=240,y=230)

        register_Button = Button(self, text="Submit", width=20).place(x=180,y=280)

        # getRecommendationButton = tk.Button(self, text="GET RECOMMENDATION", pady=20, padx=10)
        # getRecommendationButton.grid(column=1, row=1)
