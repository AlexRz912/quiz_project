import json

class User:
    """
    this class does not implement player progression as a user is only created 
    at the end of the quiz if the player decides to save his results

    """
    def __init__(self, nickname):
        self.nickname = nickname
        self.load_user_via_json()

    def load_user_via_json(self):
        try:
            with open("data/utilisateurs.json","r", encoding="utf-8") as f:
                data = json.load(f)
            if self.nickname in data:
                return data[self.nickname]
            
        except Exception as e:
            print(f"Unexpected error : {e}")

    def is_user_already_created():
        return
    
    def save_user_score_into_json():
        return
