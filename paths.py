import os
from pathlib import Path

# DataLoader paths
files_folder = os.path.abspath(os.path.dirname("files"))
FILES_FOLDER = Path(files_folder)
if "views" in str(FILES_FOLDER).split("/"):
    path_string = str(FILES_FOLDER)
    path_string = path_string[0:path_string.find("views")]
    FILES_FOLDER = Path(path_string)

GENRES_PATH = FILES_FOLDER / "files/genre.txt"


USERS_PATH = FILES_FOLDER / "files/users.txt"
ITEMS_PATH = FILES_FOLDER / "files/items2.txt"
SCORES_PATH = FILES_FOLDER / "files/u1_base_2.txt"
MOVIE_POSTERS_PATH = FILES_FOLDER / "files/movie_poster.csv"
USERNAMES_PATH = FILES_FOLDER / "files/usernames.txt"
PREFERENCES_PATH = FILES_FOLDER / "files/collab-preferences.txt"


# Images path
image_folder = os.path.abspath(os.path.dirname("images"))
IMAGE_FOLDER = Path(image_folder) / "images"
if "views" in str(IMAGE_FOLDER).split("/"):
    path_string = str(IMAGE_FOLDER)
    path_string = path_string[0:path_string.find("views")]
    IMAGE_FOLDER = Path(path_string)
#IMAGE_FOLDER = IMAGE_FOLDER / "images"

# Views path
views_folder = os.path.abspath((os.path.dirname("views")))
VIEWS_FOLDER = Path(views_folder) / "views"