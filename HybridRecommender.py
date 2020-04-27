from CollaborativeRecommender import CollaborativeRecommender
from DemographicRecommender import DemographicRecommender


class HybridRecommender():

    def __init__(self, user_id, db):
        self.user_id = user_id
        self.db = db
        self.reco = DemographicRecommender(user_id, db)
        self.collab = CollaborativeRecommender(user_id, db)
        self.recommended_items = []
        self.mix_items()


    def mix_items(self):
        self.recommended_items = self.reco.recommended_items + self.collab.recommended_items
        self.recommended_items.sort(key=lambda x: x.ratio, reverse=True)

    def weighted_mix(self):
        pass
