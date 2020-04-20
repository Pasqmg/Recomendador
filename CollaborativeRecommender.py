from datamanager.DataLoader import DataLoader
from datamanager.RecommendedItem import RecommendedItem

VERBOSE = 0
MIN_SCORE_DIFFERENCE = 40
MINIMUM_SIMILARITIES_FOR_NEIGHBOUR = 5


def calculate_variance(vector):
    # calculate mean
    m = sum(vector) / len(vector)

    # calculate variance using a list comprehension
    var_res = sum((xi - m) ** 2 for xi in vector) / len(vector)
    return var_res


class CollaborativeRecommender():

    def __init__(self, user_id, db):
        # attributes
        self.user_id = user_id
        self.user_preferences = []
        self.recommended_items = []
        self.preference_matrix = {}
        self.similarities = []
        self.neighbours = {}
        self.final_neighbours = {}

        # database
        self.db = db
        #self.db.read_all_data()

        # initialization
        self.get_preferences()
        self.fill_preference_matrix()
        self.fill_neighbours()
        self.choose_neighbours()
        self.get_neighbour_items()
        self.delete_duplicates()
        self.delete_history_items()

    def get_preferences(self):
        self.user_preferences = self.db.get_user(self.user_id).collaborative_preferences

    # fills the preference_matrix dict with the collaborative_preferences array
    # of every user except the one we are giving the recommendation to
    def fill_preference_matrix(self):
        for user_id in self.db.users_dic.keys():
            if user_id != self.user_id:
                user = self.db.get_user(user_id)
                self.preference_matrix[user_id] = user.collaborative_preferences

    def fill_neighbours(self):
        for user_id in self.preference_matrix.keys():
            # number of similar genre preferences
            equal_preferences = 0
            n_preferences = self.preference_matrix.get(user_id)
            differences = []
            for i in range(len(self.user_preferences)):
                # guarda en valor absoluto la diferencia entre el ratio de preferencia de un determinado género
                # del usuario actual con el ratio de preferencia de ese mismo género de el potencial vecino
                if self.user_preferences[i] > 0:
                    difference = abs(self.user_preferences[i] - n_preferences[i])
                    differences.append(difference)
                # if both users like the same genre, if the difference is lower than the min
                # count as a similarity
                if self.user_preferences[i] > 0 and n_preferences[i] > 0:
                    if difference <= MIN_SCORE_DIFFERENCE:
                        # the user and the potential neighbour share a common preference
                        equal_preferences += 1

            # create neighbour
            if equal_preferences > MINIMUM_SIMILARITIES_FOR_NEIGHBOUR:
                similarity_ratio = equal_preferences * (1 / sum(differences))
                self.neighbours[user_id] = Neighbour(user_id, n_preferences, similarity_ratio)
                # self.similarities.append((user_id, equal_preferences, equal_preferences*(1/sum(differences))))
        # self.similarities.sort(key=lambda x: x[2], reverse=True)

    def choose_neighbours(self):
        n_amount = 40
        similarities = []
        sum = 0
        max = 0
        for key in self.neighbours.keys():
            neigh = self.neighbours.get(key)
            similarities.append((key, neigh.similarity_ratio))
            sum += neigh.similarity_ratio
            if neigh.similarity_ratio > max:
                max = neigh.similarity_ratio
        # max normalization
        similarities = [(x[0], round(float(x[1]) / max * 100, 2)) for x in similarities]
        # normalization
        # similarities = [(x[0], round(float(x[1])/sum*100, 2)) for x in similarities]
        similarities.sort(key=lambda x: x[1], reverse=True)
        for i in range(n_amount):
            self.final_neighbours[similarities[i][0]] = self.neighbours.get(similarities[i][0])
            self.final_neighbours.get(similarities[i][0]).similarity_ratio = similarities[i][1]

    def get_neighbour_items(self):
        items = []
        for user_id in self.final_neighbours.keys():
            neighbour = self.final_neighbours.get(user_id)
            user = self.db.get_user(user_id)
            for item in user.history:
                item.ratio *= neighbour.similarity_ratio / 100
                items.append(item)
        items.sort(key=lambda x: x.id)
        self.recommended_items = items

    def delete_duplicates(self):
        dict = {}
        # get, for every item, all its scores
        for item in self.recommended_items:
            if dict.get(item.title) is None:
                list_of_ratios = []
                list_of_ratios.append(item.ratio)
                item_id = item.id
                item_genres = item.ratios
            else:
                (list_of_ratios, item_id, item_genres) = dict.get(item.title)
                list_of_ratios.append(item.ratio)
            dict[item.title] = (list_of_ratios, item_id, item_genres)

        # for items with more than one score, create a single average score
        for key in dict.keys():
            (list_of_ratios, item_id, item_genres) = dict.get(key)
            score = sum(list_of_ratios) / len(list_of_ratios)
            dict[key] = (score, item_id, item_genres)

        # for every item in dict, create a recommended item and add it to the list
        aux = []
        for key in dict.keys():
            (score, item_id, item_genres) = dict.get(key)
            reco = RecommendedItem(item_id, key, score, item_genres)
            aux.append(reco)

        # sort items by ratio
        aux.sort(key=lambda x: x.ratio, reverse=True)
        self.recommended_items = aux
        # aux.sort(key=lambda x: x.title, reverse=True)
        # title = item.title
        # print("Item is {}".format(item.title))
        # # get all equal items
        # same_items = [i for i in self.recommended_items if i.title == title]
        # same_items.append(item)
        # print("Same_items are {}".format(same_items))
        # score = 0
        # for same_item in same_items:
        #     score += same_item.ratio
        # score = score/len(same_items)
        # # create new RecommendedItem that joins all repeated HistoryItems
        # reco = RecommendedItem(item.id, item.title, score, item.ratios)
        # print("Recomended items is {}".format(reco.title))
        # aux.append(reco)
        # # update list
        # self.recommended_items = [i for i in self.recommended_items if i not in same_items]

    def delete_history_items(self):
        # delete from recommendations movies already seen by the user
        user = self.db.get_user(self.user_id)
        user_history = user.history
        if len(user_history) > 0:
            history_ids = [h.id for h in user_history]
            self.recommended_items = [x for x in self.recommended_items if x.id not in history_ids]


class Neighbour:
    def __init__(self, user_id, preferences, similarity_ratio):
        self.user_id = user_id
        self.preferences = preferences
        self.similarity_ratio = similarity_ratio

    def print(self):
        return "Neigh. {id:5d} {r:8.2f}%".format(id=self.user_id, r=self.similarity_ratio)
