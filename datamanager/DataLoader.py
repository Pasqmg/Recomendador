import random

from datamanager.HistoryItem import HistoryItem
from datamanager.Item import Item
from datamanager.Score import Score
from datamanager.User import User
from paths import GENRES_PATH, ITEMS_PATH, USERS_PATH, SCORES_PATH, PREFERENCES_PATH, USERNAMES_PATH

VERBOSE = 0


class DataLoader:

    def __init__(self):

        self.genres_path = GENRES_PATH
        self.items_path = ITEMS_PATH
        self.users_path = USERS_PATH
        self.scores_path = SCORES_PATH
        self.preferences_path = PREFERENCES_PATH
        self.usernames_path = USERNAMES_PATH

        if VERBOSE > 0:
            print(self.genres_path)
            print(self.items_path)
            print(self.users_path)
            print(self.scores_path)

        self.genres_dic = {}
        self.items_dic = {}
        self.users_dic = {}
        self.scores_dic = {}
        self.usernames_list = []

        self.read_all_data()

    def read_items(self):

        f = open(self.items_path, "r")

        for line in f.readlines():
            split = line.split()
            id = int(split[0])
            string_ratio = split[1:20]
            ratios = []
            for x in string_ratio:
                ratios.append(int(x))
            title = " "
            title = title.join(split[20:])
            item = Item(title, ratios)
            self.items_dic[id] = item
            if VERBOSE > 0:
                print("split {}".format(split))
                print("id: {}".format(id))
                print("Ratios: {}".format(ratios))
                print("Title: {}".format(title))
                print("\n")

    def read_genres(self):
        f = open(self.genres_path, "r")

        for line in f.readlines():
            split = line.split()
            id = int(split[0])
            genre = split[1]
            self.genres_dic[id] = genre
            if VERBOSE > 0:
                print("split {}".format(split))
                print("id: {}".format(id))
                print("genre: {}".format(genre))

    def read_users(self):

        f = open(self.users_path, "r")

        for line in f.readlines():
            split = line.split()
            id = int(split[0])
            age = int(split[1])
            gender = split[2]
            occupation = split[3]
            user = User(age, gender, occupation)
            self.users_dic[id] = user
            if VERBOSE > 0:
                print("split {}".format(split))
                print("id: {}".format(id))
                print("age: {}".format(age))
                print("gender: {}".format(gender))
                print("occupation: {}".format(occupation))

    def read_scores(self):

        f = open(self.scores_path, "r")

        for line in f.readlines():
            split = line.split()
            user_id = int(split[0])
            movie_id = int(split[1])
            try:
                ratio = int(split[2]) * 100 / 5
            except ValueError:
                ratio = float(split[2]) * 100 / 5

            if self.scores_dic.get(user_id) is None:
                self.scores_dic[user_id] = []
                self.scores_dic[user_id].append(Score(user_id, movie_id, ratio))
            else:
                self.scores_dic[user_id].append(Score(user_id, movie_id, ratio))

            if VERBOSE > 0:
                print("split {}".format(split))
                print("user_id: {}".format(user_id))
                print("movie_id: {}".format(movie_id))
                print("ratio: {}".format(ratio))

    def read_preferences(self):
        f = open(self.preferences_path, "r")

        for line in f.readlines():
            parts = line.split()
            user_id = int(parts[0])
            string_prefs = parts[1:20]
            prefs = []
            for x in string_prefs:
                prefs.append(float(x))

            self.get_user(user_id).collaborative_preferences = prefs
            print("user {} prefs: {}".format(user_id, self.get_user(user_id).collaborative_preferences))

            if VERBOSE > 0:
                print("parts {}".format(parts))
                print("user_id: {}".format(user_id))
                print("prefs: {}".format(prefs))

    def read_usernames(self):
        f = open(self.usernames_path, "r")

        for line in f.readlines():
            parts = line.split()
            user_id = int(parts[0])
            username = parts[1]
            self.get_user(user_id).username = username
            self.usernames_list.append(username)

    def read_all_data(self):
        self.read_genres()
        self.read_items()
        self.read_users()
        self.read_scores()
        self.fill_history()
        self.read_preferences()
        self.read_usernames()
        # necessary only once
        #self.fill_preferences()

    # Fills the attribute history of every user in the user_dic
    def fill_history(self):

        for user_id in self.users_dic.keys():
            user = self.users_dic.get(user_id)
            user_scores = self.scores_dic.get(user_id)
            if user_scores is not None:
                for score in user_scores:
                    title = self.items_dic.get(score.item_id).title
                    genres = self.items_dic.get(score.item_id).ratios
                    history_item = HistoryItem(score.item_id, title, score.ratio, genres)
                    user.history.append(history_item)

    # Fills the attribute collaborative_preferences of every user in the user_dic
    def fill_preferences(self):
        min_ratio = 80
        for user_id in self.users_dic.keys():
            user = self.users_dic.get(user_id)
            # if the user has a history, generate preferences based on it
            if len(user.history) > 0:
                # the following structure ensures that the min_ratio selected is adequate for
                # users that have given low scores to movies too
                try:
                    user.collaborative_preferences = self.get_user_i_preferences(user_id, min_ratio)
                except ZeroDivisionError:
                    try:
                        user.collaborative_preferences = self.get_user_i_preferences(user_id, min_ratio - 10)
                    except ZeroDivisionError:
                        try:
                            user.collaborative_preferences = self.get_user_i_preferences(user_id, min_ratio - 20)
                        except ZeroDivisionError:
                            try:
                                user.collaborative_preferences = self.get_user_i_preferences(user_id, min_ratio - 30)
                            except ZeroDivisionError:
                                try:
                                    user.collaborative_preferences = self.get_user_i_preferences(user_id,
                                                                                                 min_ratio - 40)
                                except ZeroDivisionError:
                                    try:
                                        user.collaborative_preferences = self.get_user_i_preferences(user_id,
                                                                                                     min_ratio - 50)
                                    except ZeroDivisionError:
                                        try:
                                            user.collaborative_preferences = self.get_user_i_preferences(user_id,
                                                                                                         min_ratio - 60)
                                        except ZeroDivisionError:

                                            user.collaborative_preferences = self.get_user_i_preferences(user_id,
                                                                                                         min_ratio=0)

            # if it is a new user, generate preferences randomly
            else:
                user.collaborative_preferences = self.get_user_i_random_preferences(user_id)

            self.save_preferences(user_id, user.collaborative_preferences)
        # end of for loop

    # Given a user_id, returns the corresponding User object
    def get_user(self, user_id):
        return self.users_dic.get(user_id)

    def print_user_preferences(self, user_id):
        string = "Collaborative preferences:\n\n"
        preferences = self.get_user(user_id).collaborative_preferences
        for i in range(1, len(preferences)):
            genre = self.genres_dic.get(i)
            score = preferences[i]
            string += "{g:25s}\t{s:3.0f}\n".format(g=genre, s=score)
        return string

    # traverses the user dictionary and returns a list with all occupations
    def get_occupation_list(self):
        occupation_list = []
        for u in self.users_dic.values():
            if VERBOSE > 0:
                ("User occupation is {}, list is {}".format(u.occupation, occupation_list))
            if u.occupation not in occupation_list:
                occupation_list.append(u.occupation)
        occupation_list.sort()
        if VERBOSE > 0:
            print("Final list {}".format(occupation_list))
        return occupation_list

    # Given a user_id and a minimum score, returns the preferences of such user, based on the scores given
    # to its history items
    def get_user_i_preferences(self, user_id, min_ratio=0):

        u = self.users_dic.get(user_id)
        preferences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Get user history
        history = u.history
        for history_item in history:
            movie = self.items_dic.get(history_item.id)
            # if the score given to the movie is higher or equal to the minimum
            if history_item.ratio >= min_ratio:
                # add the movie genres to the user preferences array
                preferences = [sum(x) for x in zip(preferences, movie.ratios)]

        preferences = [round(float(i) / max(preferences) * 100, 2) for i in preferences]
        final_preferences = []
        for val in preferences:
            if val > 10.00:
                val = round(val, 0)
            else:
                val = 0.0
            final_preferences.append(val)
        return final_preferences

    # Given a user_id, generates random preferences
    def get_user_i_random_preferences(self, user_id):
        u = self.users_dic.get(user_id)
        preferences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # fill between 5 to 12 random genres
        num_preferences = random.randint(5, 13)
        # keep track of already chosen genres
        selected_genres = []
        for i in range(num_preferences):

            # choose genre
            genre = random.randint(1, 18)
            while genre in selected_genres:
                genre = random.randint(1, 18)

                # add genre to already chosen genres list
            selected_genres.append(genre)

            # choose score for that genre
            score = random.randint(11, 100)

            # update preferences array
            preferences[genre] = score

        return preferences

    # Given a range of ages, list of occupations and minimum scores, returns the preferences of the
    # set of users that match the given age range and or occupations
    def get_user_preferences(self, ini_age=0, end_age=100, min_ratio=0, occupations=[], weighted=False):

        users = []
        preferences = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Store all users that match the parameters
        for user_id in self.users_dic.keys():
            u = self.users_dic.get(user_id)
            if u.age >= ini_age and u.age <= end_age:
                if not occupations:
                    users.append(u)
                elif u.occupation in occupations:
                    # print("Users occupation {} vs occupation {}".format(u.occupation, occupation))
                    # if u.occupation == occupation:
                    users.append(u)

        print("Amount of users that meet parameters: {}".format(len(users)))
        # Analyze their preferences
        for u in users:
            # Get user history
            history = u.history
            for history_item in history:
                movie = self.items_dic.get(history_item.id)
                if history_item.ratio >= min_ratio:
                    if weighted:
                        weighted_ratios = [x * history_item.ratio for x in movie.ratios]
                        preferences = [sum(x) for x in zip(preferences, weighted_ratios)]
                    else:
                        preferences = [sum(x) for x in zip(preferences, movie.ratios)]

        norm = [round(float(i) / sum(preferences) * 100, 2) for i in preferences]

        mapping = []
        for i in range(len(norm)):
            mapping.append((self.genres_dic.get(i), norm[i]))
        # max_norm = [round(float(i)/max(preferences),2) for i in preferences]

        return mapping, preferences

    # Returns the genres to which a movie belongs
    def get_movie_genres(self, item_id):
        movie = self.items_dic.get(item_id)
        genres = movie.ratios
        string = ""
        for key in self.genres_dic.keys():
            if genres[key] != 0:
                string += "\t-" + self.genres_dic.get(key) + "\n"
        return string

    # Returns the average score of an item based on the user given scores
    def get_movie_avg_score(self, item_id):
        scores = []
        for user_id in self.scores_dic.keys():
            list_of_scores = self.scores_dic.get(user_id)
            for s in list_of_scores:
                if s.item_id == item_id:
                    scores.append(s.ratio)
        try:
            avg_score = sum(scores) / len(scores)
        except ZeroDivisionError:
            avg_score = 0
        return avg_score

    # Returns the movie title, its average score and its genres
    def get_movie_info(self, item_id):
        movie = self.items_dic.get(item_id)
        return [movie.title, self.get_movie_avg_score(item_id), self.get_movie_genres(item_id)]

    # Returns an ordered list presenting, for every item in the DB, its title together
    # with the average score of the item, calculated from the scores given by users
    def get_movies_by_score(self):
        all_scores = []
        for key in self.items_dic.keys():
            info = self.get_movie_info(key)
            all_scores.append((info[0], info[1]))
        all_scores.sort(key=lambda x: x[1], reverse=True)
        return all_scores

    # Given a user id, a movie id and a score, it saved the movie score in the corresponding file
    # and updates all data
    def save_score(self, user_id, movie_id, score):
        outF = open(self.scores_path, "a")
        score_base_5 = score * 5 / 10
        line = str(user_id) + "\t" + str(movie_id) + "\t" + str(score_base_5)
        # write line to output file
        outF.write(line)
        outF.write("\n")
        outF.close()

        if VERBOSE > 1:
            print("\n")
            print(f"User {user_id:3d} saved a review for movie {movie_id:4d} with score {score:2d}")

        #If the user liked the movie update user collaborative preferences
        # The idea behind this is to have better collaborative recommendations
        # as the user interacts with the system
        if score >= 5:

            old_preferences = self.get_user(user_id).collaborative_preferences
            movie_genres = self.items_dic.get(movie_id).ratios

            # Add to user old preferences a value between 1 to 5 in every genre
            # that the liked movie has. The value will be equivalent to the score
            # given by the user, being 5 -> 1 and 10 -> 5.
            movie_genres = [val*score_base_5 for val in movie_genres]

            new_preferences = [min(sum(x), 100) for x in zip(old_preferences, movie_genres)]

            if VERBOSE > 1:
                print(f"User {user_id:3d} preferences updated:")
                print(f"Old preferences: {old_preferences}")
                print(f"New preferences: {new_preferences}")
                print("\n")

            # Update preferences in the collab-preferences file
            # read preferences file
            with open(self.preferences_path, "r") as f:
                lines = f.readlines()
            # save all lines except the one corresponding to current user's preferences
            lines_to_write = []
            for line in lines:
                parts = line.split()
                id = int(parts[0])
                if id != user_id:
                    lines_to_write.append(line)
            # rewrite all other preferences
            with open(self.preferences_path, "w") as f:
                for line in lines_to_write:
                    f.write(line)
            # add new user preferences
            self.save_preferences(user_id, new_preferences)

        self.read_all_data()

    def save_preferences(self, user_id, preferences):
        outF = open(self.preferences_path, "a")
        pref_string = ""
        for val in preferences:
            pref_string += str(val) + " "
        line = str(user_id) + "\t" + pref_string
        outF.write(line)
        outF.write("\n")
        outF.close()

    def save_user(self, username, age, gender, occupation, preferences=None):
        outF = open(self.users_path, "a")
        user_id = len(self.users_dic) + 1
        line = str(user_id) + "\t" + str(age) + "\t" + str(gender) + "\t" + occupation
        outF.write(line)
        outF.write("\n")
        outF.close()

        outF = open(self.usernames_path, "a")
        line = str(user_id) + "\t" + str(username)
        outF.write(line)
        outF.write("\n")
        outF.close()

        if preferences != None:
            # save user defined preferences
            self.save_preferences(user_id, preferences)
        else:
            # create and save random user preferences
            random_preferences = self.get_user_i_random_preferences(user_id)
            self.save_preferences(user_id, random_preferences)

        self.read_all_data()

    # Preferences [0.0, 100.0,  29.0, 0.0, 29.0,  59.0,  29.0,  0.0, 71.0,  0.0,  0.0,  0.0,  0.0, 24.0,  59.0,  41.0,  82.0,  24.0, 0.0]
