
class Item:

    def __init__(self, title, ratios):
        self.title = title
        self.ratios = ratios

    def print(self):
        return "Title: {}, genres: {}".format(self.title, self.ratios)

