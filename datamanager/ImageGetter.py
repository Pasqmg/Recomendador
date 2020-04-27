import os

import PIL
from PIL import Image
import requests
from io import BytesIO
import pandas
from paths import IMAGE_FOLDER, MOVIE_POSTERS_PATH


class ImageGetter:

    def __init__(self, movie_id, title=None):
        self.path_to_csv = MOVIE_POSTERS_PATH
        self.df = pandas.read_csv(self.path_to_csv)
        if self.df is None:
            print("Could not open df")
        indexes = self.df["movie_id"].tolist()
        print("Movie_id: {}".format(movie_id))

        movie_name = str(movie_id) + ".jpg"
        save_img_path = IMAGE_FOLDER / movie_name

        if not os.path.exists(save_img_path):
            try:
                pos = indexes.index(movie_id)
                urls = self.df["poster_url"].tolist()
                url = urls[pos]
                #print("pos", pos)
                #print(url)
                response = requests.get(url)
                #print(response)

                self.img = Image.open(BytesIO(response.content))

                self.img.save(save_img_path)
                print("Image for movie {} saved".format(movie_id))
            except ValueError:
                print("No url for movie {}".format(movie_id))

            except PIL.UnidentifiedImageError:
                print("Cannot identify image file for movie {}".format(movie_id))
        else:
            print("Image for movie {} is already downloaded".format(movie_id))
        print("\n")


if __name__ == "__main__":
    i = ImageGetter(30)
