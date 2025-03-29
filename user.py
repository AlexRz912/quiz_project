import json
from datetime import date

class User:
    """
    this class does not implement player progression handling, takes the score as a parameter
    as a user is only created at the end of the quiz if the player decides to save his results
    """
    def __init__(self, nickname, score, date):
        self.nickname = nickname
        self.score = score
        self.date = date
        self.users_data = {}

    def json_load_all_users(self):
        try:
            with open("data/utilisateurs.json","r", encoding="utf-8") as f:
                data = json.load(f)
            return data
            # print(data[self.nickname])

        except Exception as e:
            print(f"Unexpected error : {e}")

    def users_exists(self):
        """I need it in order not to delete user data before saving a new user"""
        return self.nickname in self.users_data

    def json_save_user(self):
        """
        I think of saving the user if it doesn't exist and saving the score for the user as 
        two different functionnalities
        """
        self.users_data[self.nickname] = self.format_user_for_json()
        self.save_users_data()
            
    
    def json_save_score(self):
        """ saves score for user in exactly the same way if it's a new user or old user as the new user"""
        
        self.users_data[self.nickname]['scores'].append({
            'theme': None,
            'score': self.score, 
            'date':  self.date
        })
        self.save_users_data()

    
    def format_user_for_json(self):
        return {
            'scores': []
        }

    def save_users_data(self):
        """ used for saving a new user and saving a new score """

        try:
            with open("data/utilisateurs.json", "w", encoding="utf-8") as f:
                json.dump(self.users_data, f, indent=4, ensure_ascii=False)
        except Exception as e: 
            print(f"error while saving user {e}")