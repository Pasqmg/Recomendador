from datamanager.DataLoader import DataLoader
from datamanager.RecommendedItem import RecommendedItem
from datamanager.UserType import *
from datamanager.User import User

VERBOSE = 0

class DemographicRecommender():

    def __init__(self, user_id, db):
        self.user_id = user_id
        self.user_type = None
        self.recommended_items = []
        self.types = [Geek(), RomanticComedy(), OldGlory(), LawHead(), Purist(), Scientist(),
                      KidsType(), MaleTeen(), FemaleTeen(), StandardAdultMale(), StandardAdultFemale(),
                      YoungMan(), YoungWoman(), OldMan(), OldWoman(), ]
        self.db = db
        #self.db.read_all_data()

        # initialization
        self.classify_user()
        self.get_recommendations()

    # For all types, check if the user belongs to them
    def classify_user(self):
        user = self.db.get_user(self.user_id)
        for type in self.types:
            if type.check_user(user):
                print("User {} is of type {}".format(self.user_id, type.name))
                self.user_type = type
                user.demographic_preferences = type.ratios

    # Assign a value to all movies in the DB according
    # to the self.user_type preferences and orders them
    def get_recommendations(self):
        for key in self.db.items_dic.keys():
            movie = self.db.items_dic.get(key)
            recommendation = RecommendedItem(key, movie.title, self.compute_ratio(movie), movie.ratios)
            self.recommended_items.append(recommendation)
        self.recommended_items.sort(key=lambda x: x.ratio, reverse=True)

        # delete from recommendations movies already seen by the user
        user = self.db.get_user(self.user_id)
        user_history = user.history
        if len(user_history) > 0:
            history_ids = [h.id for h in user_history]
            self.recommended_items = [x for x in self.recommended_items if x.id not in history_ids]



    def compute_ratio(self, movie):
        # Scores of the movie:
        sf = None   # movie contains forbidden genres
        s1 = 0   # movie genres that meet main preferences of the user type
        s2 = 0   # movie genres that meet secondary preferences of the user type

        ratios = movie.ratios   # genres of the movie to evaluate
        base = self.user_type.ratios    # genre preferences of the user type

        # returns True if the movie is safe, false otherwise
        if not self.user_type.check_forbidden_genre(ratios):
            # the movie contains genres that can not be recommended to the user type
            sf = 0
        else:
            sf = 1

        for i in range(len(ratios)):
            if base[i] > 0 and ratios[i] > 0:
                if base[i] > 1:
                    # movie contains a main preferred genre
                    s1 += 1
                else:
                    # movie contains a secondary preferred genre
                    s2 += 1

        # adjust score to amount of main genres that the movie matches
        s1 = s1/self.user_type.get_main_genres_amount()
        s2 = s2/self.user_type.get_secondary_genres_amount()

        # weigths determine the importance of main and secondary genres
        w1 = 0.8
        w2 = 0.2
        score = round(((w1*s1 + w2*s2)*sf)*100)
        if VERBOSE > 0:
            ("Movie {} has ratio {}".format(movie.title, score))
        return score

