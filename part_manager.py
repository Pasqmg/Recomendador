import random
import tkinter as tk
from tkinter import ttk

from CollaborativeRecommender import CollaborativeRecommender
from DemographicRecommender import DemographicRecommender
from datamanager.DataLoader import DataLoader
from new_user_page import NewUserPage

LARGE_FONT = ("Verdana", 12)


class MovieBingeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        # DataLoader
        db = DataLoader()
        db.read_all_data()
        all_scores = []
        for key in db.items_dic.keys():
            info = db.get_movie_info(key)
            all_scores.append((info[0], info[1]))
        all_scores.sort(key = lambda x: x[1], reverse=True)
        for i in all_scores:
            print(i)

        # user_id = 30
        # print(db.get_user(user_id).collaborative_preferences)
        # collab = CollaborativeRecommender(user_id, db)
        # for key in collab.final_neighbours.keys():
        #     print(key, collab.final_neighbours.get(key).print())
        # items = collab.recommended_items
        # for i in items:
        #     print(i.print())


        """
        norm = db.get_user_i_preferences(user_id=8, min_ratio=80)
        #print("Mapping {}".format(mapping))
        print("Preferences {}".format(norm))

        norm = db.get_user(8).collaborative_preferences
        print("Preferences {}".format(norm))
        
        user_id = 41
        user = db.get_user(user_id)
         #random.randint(0, len(db.users_dic))
        print("User id:",user_id)

        reco = DemographicRecommender(user_id)

        reco.classify_user()

        reco.get_recommendations()

        print("History items:")
        print("===========================")
        for i in range(len(user.history)):
            print(i + 1, " ", user.history[i].print())

        print("Recommended items:")
        print("===========================")
        for i in range(250):
            print(i+1," ",reco.recommended_items[i].print())
        """


        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "MovieBinge")
        # tk.Tk.iconbitmap(self, "@/Users/pasqualmartigimeno/PycharmProjects/recomendador/files/favicon.ico")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [StartPage, PageOne, PageTwo, NewUserPage] :

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        newUserButton = tk.Button(self, text="NEW USER",
                                  command=lambda: controller.show_frame(NewUserPage))
        newUserButton.pack()

        page2Button = tk.Button(self, text="GO TO PAGE 2",
                               command=lambda: controller.show_frame(PageTwo))
        page2Button.pack()

        #getRecommendationButton = tk.Button(self, text="GET RECOMMENDATION", pady=20, padx=10)
        #getRecommendationButton.grid(column=1, row=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        backButton = tk.Button(self, text="BACK TO HOME",
                                  command=lambda: controller.show_frame(StartPage))
        backButton.pack()

        page2Button = tk.Button(self, text="GO TO PAGE 2",
                               command=lambda: controller.show_frame(PageTwo))
        page2Button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        backButton = tk.Button(self, text="BACK TO HOME",
                                  command=lambda: controller.show_frame(StartPage))
        backButton.pack()

        backButton2 = tk.Button(self, text="BACK TO PAGE 1",
                               command=lambda: controller.show_frame(PageOne))
        backButton2.pack()

app = MovieBingeApp()
#app.title("MovieBinge")
#app.geometry("500x500")
app.mainloop()
# Create window object


# print("Number of items {}".format(len(db.items_dic)))
# print("Number of users {}".format(len(db.users_dic)))
# num_scores = 0
# for score_list in db.scores_dic.values():
#     num_scores += len(score_list)
# print("Number of scores {}".format(num_scores))

# app = Tk();
# app.title("MovieBinge")
# app.geometry('700x350')

# Start program
# app.mainloop();
