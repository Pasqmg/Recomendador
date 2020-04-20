from datamanager.Item import Item


class RecommendedItem(Item):

    def __init__(self, id, title, ratio, genres):
        super().__init__(title, genres)
        self.id = id
        self.ratio = ratio

    def __lt__(self, other):
        if self.ratio > other.ratio:
            return self
        else:
            return other

    def print(self):
        return "{t:50s} {r:8.0f}%".format(t=self.title, r=self.ratio)
