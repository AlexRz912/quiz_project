class PlayerProgression:
    """ 
    I use a player progression class instead of user because I'm only dealing with saving nickname
    at the end of the program, the user is a simple string called nickname. Most of the class
    is dealing with player score and correct/wrong answers
    """
    def __init__(self):

        self.score = 0
        self.answers = {
            "correct_answers": {},
            "wrong_answers": {}
        }
        self.nickname = ""

    def increment_score(self):
        """ implement  """
        self.score += 1

    def add_answer_to_progression(self, answer, question_index, is_correct=False):
        """ self explanatory """
        if is_correct:
            self.answers["correct_answers"][question_index] = answer
        else:
            self.answers["wrong_answers"][question_index] = answer

    