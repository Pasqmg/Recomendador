
class User:

    def __init__(self, age, gender, occupation):
        self.age = age
        self.gender = gender
        self.occupation = occupation

        # Watched movie history
        self.history_num = None
        self.history = []

        # Demographic recommendation
        self.user_type = None
        self.demographic_preferences = []

        # Collaborative recommendation
        self.collaborative_preferences = []
        self.neighbours = []

