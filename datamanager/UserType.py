VERBOSE = 0

class UserType():

    def __init__(self):
        self.name = "No Name"
        self.ratios = []
        self.age_range = (None, None)
        self.occupations = None
        self.gender = None
        self.forbidden_genre = []

    def get_main_genres_amount(self):
        return len([x for x in self.ratios if x == 2])

    def get_secondary_genres_amount(self):
        y = len([x for x in self.ratios if x == 1])
        if y == 0:
            y = 1
        return y

    def check_age(self, age):
        return self.age_range[0] <= age <= self.age_range[1]

    def check_occupation(self, occupation):
        if self.occupations is not None:
            return occupation in self.occupations
        else:
            return True

    def check_gender(self, gender):
        if self.gender is not None:
            return gender == self.gender
        else:
            return True

    # If the type has restricted genres, it will check that a
    # recommended movie does not contain any of them
    def check_forbidden_genre(self, movie_ratios):
        for position in self.forbidden_genre:
            if movie_ratios[position] != 0:
                return False
        return True

    # Checks user attributes to determine if it belongs to this type
    def check_user(self, user):
        a = self.check_age(user.age)
        b = self.check_gender(user.gender)
        c = self.check_occupation(user.occupation)
        if VERBOSE > 0:
            print("Testing user {} against type \"{}\"".format(user, self.name))
            if not a:
                 print("User is not in the adequate age range")
            if not b:
                 print("User is not of the adequate gender")
            if not c:
                 print("User does not have adequate occupation")
            print("\n")
        return a and b and c

# number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#self.ratios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
class KidsType(UserType):
    # user 30 is Kids
    def __init__(self):
        super().__init__()
        self.name = "Kids"
        # number      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.age_range = (0, 12)
        self.forbidden_genre = [10, 11, 17]  # war, horror, film-noir


class MaleTeen(UserType):

    def __init__(self):
        super().__init__()
        self.name = "Male teen"
        # number      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 1, 0, 0, 1, 2, 0, 0, 0, 0,  0,  2,  0,  0,  0,  2,  0,  0,  0]
        self.age_range = (13, 20)
        self.gender = "M"


class FemaleTeen(UserType):

    def __init__(self):
        super().__init__()
        self.name = "Female teen"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 1, 2, 0, 0, 0, 0,  0,  2,  1,  0,  2,  0,  0,  0,  0]
        self.age_range = (13, 20)
        self.gender = "F"

        # [ (0,unknown), (1 Action), (2 Adventure), (3 Animation), (4 Children's), (5 Comedy), (6 Crime), (7 Documentary),
        #   (8 Drama), (9 Fantasy), (10 Film-Noir), (11 Horror), (12 Musical), (13 Mystery), (14 Romance), (15 Sci-Fi),
        #   (16 Thriller), (17 War), (18 Western) ]
class YoungMan(UserType):

    def __init__(self):
        super().__init__()
        self.name = "Young man"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 2, 2, 0, 0, 1, 0, 0, 0, 1,  0,  0,  0,  0,  0,  2,  0,  0,  0]
        self.age_range = (21, 34)
        self.gender = "M"


class YoungWoman(UserType):

    def __init__(self):
        super().__init__()
        self.name = "Young woman"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1,  0,  0,  2,  2,  2,  0,  0,  0,  0]
        self.age_range = (21, 34)
        self.gender = "F"


class StandardAdultMale(UserType):
    # user  is
    def __init__(self):
        super().__init__()
        self.name = "Standard adult male"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 2, 1, 0, 0, 0, 0, 0, 2, 0,  0,  0,  0,  1,  0,  0,  2,  2,  0]
        self.age_range = (35, 50)
        self.gender = "M"


class StandardAdultFemale(UserType):
    # user  is
    def __init__(self):
        super().__init__()
        self.name = "Standard adult female"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 1, 0, 0, 0, 2, 0, 2, 0,  0,  0,  0,  1,  2,  0,  2,  0,  0]
        self.age_range = (35, 50)
        self.gender = "F"


class OldMan(UserType):
    # user  is
    def __init__(self):
        super().__init__()
        self.name = "Old man"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0,  2,  0,  0,  0,  0,  0,  0,  2,  2]
        self.age_range = (51, 120)
        self.gender = "M"


class OldWoman(UserType):
    # user  is
    def __init__(self):
        super().__init__()
        self.name = "Old woman"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  2,  0,  1,  1,  2,  0,  0,  0,  2]
        self.age_range = (51, 120)
        self.gender = "F"


class Geek(UserType):
    # user 41 is geek
    def __init__(self):
        super().__init__()
        self.name = "Geek"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 2, 2, 0, 0, 0, 0, 0, 2,  0,  0,  0,  0,  0,  2,  1,  1,  0]
        self.age_range = (21, 35)
        self.occupations = ["programmer", "engineer"]


class RomanticComedy(UserType):
    # user 62 is Romantic-comedy
    def __init__(self):
        super().__init__()
        self.name = "Romantic-comedy"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 0, 2, 0, 0, 2, 0,  0,  0,  1,  0,  2,  0,  0,  0,  0]
        self.age_range = (21, 35)
        self.occupations = ["artist", "writer", "student", "marketing", "administrator", "educator"]
        self.gender = "F"


class OldGlory(UserType):
    # user 234 is Old glory
    def __init__(self):
        super().__init__()
        self.name = "Old glory"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 1, 0, 0, 0, 0, 0, 0, 2, 0,  0,  0,  0,  0,  0,  0,  0,  2,  2]
        self.age_range = (50, 120)
        self.occupations = ["retired", "executive", "salesman", "librarian"]
        self.gender = "M"


class LawHead(UserType):
    # user  is Law head
    def __init__(self):
        super().__init__()
        self.name = "Law head"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 0, 0, 2, 0, 1, 0,  0,  0,  0,  2,  0,  0,  1,  0,  0]
        self.age_range = (26, 100)
        self.occupations = ["lawyer"]


class Purist(UserType):
    # user 39 is Purist
    def __init__(self):
        super().__init__()
        self.name = "Purist"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 0, 0, 0, 2, 1, 0,  2,  0,  0,  0,  0,  0,  2,  0,  0]
        self.age_range = (30, 60)
        self.occupations = ["entertainment", "writer", "retired"]
        self.gender = "M"


class Scientist(UserType):
    # user  is Scientist
    def __init__(self):
        super().__init__()
        self.name = "Scientist"
        #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.ratios = [0, 0, 0, 0, 0, 0, 0, 2, 0, 0,  0,  0,  0,  0,  0,  2,  0,  0,  0]
        self.age_range = (21, 120)
        self.occupations = ["scientist", "doctor"]




# [ (0,unknown), (1 Action), (2 Adventure), (3 Animation), (4 Children's), (5 Comedy), (6 Crime), (7 Documentary),
#   (8 Drama), (9 Fantasy), (10 Film-Noir), (11 Horror), (12 Musical), (13 Mystery), (14 Romance), (15 Sci-Fi),
#   (16 Thriller), (17 War), (18 Western) ]
# number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#self.ratios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]




# class (UserType):
#     # user  is
#     def __init__(self):
#         super().__init__()
#         self.name = ""
#         #number       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
#         self.ratios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
#         self.age_range = (0, 100)
#         self.occupations = []
#         self.gender =