import json

class User:
    """
    this class does not implement player progression handling, takes the score as a parameter
    as a user is only created at the end of the quiz if the player decides to save his results
    """
    def __init__(self, nickname, score):
        self.nickname = nickname
        self.score = score
        self.date = None
        self.users_data = {}

    def json_load_user_if_exists(self):
        try:
            with open("data/utilisateurs.json","r", encoding="utf-8") as f:
                data = json.load(f)
            return data[self.nickname]

        except KeyError:
            print(f"User doesn't exist")
            with open("data/utilisateurs.json","r", encoding="utf-8") as f:
                data = json.load(f)
            return data
            # print(data[self.nickname])

        except Exception as e:
            print(f"Unexpected error : {e}")

    
    def json_save_user(self):
        """
        I think of saving the user if it doesn't exist and saving the score for the user as 
        two different functionnalities
        """
        self.users_data[self.nickname] = self.format_user_for_json()
        print(self.users_data)
        try:
            with open("data/utilisateurs.json", "w", encoding="utf-8") as f:
                json.dump(self.users_data, f, indent=4, ensure_ascii=False)
        except Exception as e: 
            print(f"error while saving user {e}")
            
    
    def json_save_score(self):
        """ saves score for user in exactly the same way if it's a new user or old user """
        return

    def format_user_for_json(self):
        return {
            'scores': [
                {
                    'theme': None,
                    'score': None, 
                    'date':  None
                }
            ]
            
        }