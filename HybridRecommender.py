from CollaborativeRecommender import CollaborativeRecommender
from DemographicRecommender import DemographicRecommender

VERBOSE = 1


class HybridRecommender:

    def __init__(self, user_id, db):
        self.user_id = user_id
        self.db = db
        self.demo = DemographicRecommender(user_id, db)
        self.collab = CollaborativeRecommender(user_id, db)
        self.recommended_items = []
        self.dynamic_weighted_mix()

    # Mixes items from Demographic and Collaborative recommenders.
    # If a duplicate is found, the recommended item with higher ratio is kept.
    def mix_items(self):
        final_items = []
        for item in self.demo.recommended_items:
            r1 = item.ratio
            duplicates = [x for x in self.collab.recommended_items if x.id == item.id]
            if len(duplicates) > 1:
                print(f"Something went wrong with duplicates:")
                print(f"Original item: {item.print()}")
                print(f"List:")
                for x in duplicates:
                    print(x.print())
            if len(duplicates) == 0:
                final_items.append(item)
            else:
                r2 = duplicates[0].ratio
                if r1 >= r2:
                    final_items.append(item)
                else:
                    final_items.append(duplicates[0])
        final_items.sort(key=lambda x: x.ratio, reverse=True)
        self.recommended_items = final_items

    # Mixes items from both recommenders, multiplying their ratios by a predefined weight.
    # Duplicated items have their ratios slightly increased if they have good punctuations.
    def weighted_mix(self, demo_w=0.4, collab_w=0.6):
        final_items = []
        # Apply weighting
        for item in self.demo.recommended_items:
            item.ratio = item.ratio * demo_w
        for item in self.collab.recommended_items:
            item.ratio = item.ratio * collab_w
        # Choose items
        for item in self.demo.recommended_items:
            r1 = item.ratio
            duplicates = [x for x in self.collab.recommended_items if x.id == item.id]
            if len(duplicates) > 1:
                print(f"Something went wrong with duplicates:")
                print(f"Original item: {item.print()}")
                print(f"List:")
                for x in duplicates:
                    print(x.print())
            if len(duplicates) == 0:
                final_items.append(item)
            else:
                r2 = duplicates[0].ratio
                if r1 >= r2:
                    # If the other ratio is 0, include item with ratio > 0 unmodified
                    if r2 == 0:
                        final_items.append(item)
                    # Otherwise, compute the average of the ratios and increase item ratio accordingly
                    else:
                        mean = (r1 + r2) / 2
                        if 1 <= mean < 15:
                            item.ratio *= 1.1
                        elif 15 <= mean < 30:
                            item.ratio *= 1.2
                        elif 30 <= mean < 50:
                            item.ratio *= 1.25
                        else:
                            item.ratio *= 1.1
                        if item.ratio > 100:
                            item.ratio = 100

                        final_items.append(item)
                    if r1 > 30:
                        if r2 > 20:
                            item.ratio = item.ratio + 0.2 * item.ratio

                else:
                    # If the other ratio is 0, include item with ratio > 0 unmodified
                    if r1 == 0:
                        final_items.append(duplicates[0])
                    else:
                        # Otherwise, compute the average of the ratios and increase item ratio accordingly
                        mean = (r1 + r2) / 2
                        if 1 <= mean < 15:
                            duplicates[0].ratio *= 1.1
                        elif 15 <= mean < 30:
                            duplicates[0].ratio *= 1.2
                        elif 30 <= mean < 50:
                            duplicates[0].ratio *= 1.25
                        else:
                            duplicates[0].ratio *= 1.1
                        if duplicates[0].ratio > 100:
                            duplicates[0].ratio = 100

                        final_items.append(duplicates[0])
        final_items.sort(key=lambda x: x.ratio, reverse=True)
        self.recommended_items = final_items

    # Mixes items from both recommenders, multiplying their ratios by a dynamically calculated weight.
    # Duplicated items have their ratios slightly increased.
    def dynamic_weighted_mix(self):
        # Calculate weights dynamically

        # Weight of collaborative recommender will depend on number oh history items
        # as well as number of neighbours

        # 20 is the minimum number of scores a user can have, unless it's a new user
        try:
            user_score_amount = len(self.db.scores_dic.get(self.user_id))
        except TypeError:
            # User has no reviews
            user_score_amount = 0
        reviews_weight = user_score_amount/20
        if reviews_weight > 1:
            reviews_weight = 1.0

        # 40 is the normal amount of neighbours
        user_neigh_amount = len(self.collab.final_neighbours)
        neigh_weight = user_neigh_amount/40

        # Give 70% importance to neighbours and 30% to amount of reviews
        collab_weight = 0.7 * neigh_weight + 0.3 * reviews_weight

        # Give collaboratory recommender a maximum of 60% of the total weight
        final_collab_weight = 0.6 * collab_weight
        demo_weight = 1 - final_collab_weight

        if VERBOSE > 0:
            print(f"User {self.user_id:3d} has {user_score_amount:3d} reviews, giving them a {reviews_weight:3.2f} reviews_weight")
            print(f"User {self.user_id:3d} has {user_neigh_amount:3d} neighbours, giving them a {neigh_weight:3.2f} neigh_weight")
            print(f"User {self.user_id:3d} Collab weight is {collab_weight:3.2f}")
            print(f"User {self.user_id:3d} final weights are demo: {demo_weight:3.2f} collab: {final_collab_weight:3.2f}")
            print("\n")

        self.weighted_mix(demo_w=demo_weight, collab_w=collab_weight)
