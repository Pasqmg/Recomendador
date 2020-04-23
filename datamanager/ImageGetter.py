from PIL import Image
import requests
from io import BytesIO
import pandas


class ImageGetter:

    def __init__(self, movie_id, title):
        self.path_to_csv = "/home/pasqual/PycharmProjects/Recomendador/files/movie_poster.csv"
        self.df = pandas.read_csv(self.path_to_csv)
        indexes = self.df["movie_id"].tolist()
        try:
            pos = indexes.index(movie_id)
            urls = self.df["poster_url"].tolist()
            url = urls[pos]
            print("pos", pos)
            print(url)
            response = requests.get(url)
            try:
                self.img = Image.open(BytesIO(response.content))
                self.img.save("/home/pasqual/PycharmProjects/Recomendador/images/" + title + ".jpg")
            except:
                pass
        except:
            pass

        #img.show()

if __name__ == "__main__":
    i = ImageGetter(30)
