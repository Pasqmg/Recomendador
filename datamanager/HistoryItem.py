from datamanager.Item import Item


class HistoryItem(Item):

    def __init__(self, id, title, ratio, genres):
        super().__init__(title, genres)
        self.id = id
        self.ratio = ratio

    def print(self):
        return "{t:50s} {r:8.0f}".format(t=self.title, r=self.ratio)