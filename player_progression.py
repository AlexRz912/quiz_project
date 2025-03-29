class PlayerProgression:
    """ 
    Deals with anything related to player quiz progression outside the question loop
    I use a Player progression class and I separate it from a User Class because I'm only dealing 
    with saving nickname at the end of the program.  
    Most of the class is dealing with player score and correct/wrong answers, 
    and a User won't even be created if the player decides not to.
    """

    def __init__(self):
        """ I've divided those for easier access later """
        self.score = 0
        self.answers = {
            "correct_answers": {},
            "wrong_answers": {}
        }
        self.nickname = ""

    def increment_score(self):
        """ self explanatory  """
        self.score += 1

    def add_answer_to_progression(self, answer, question_index, is_correct=False):
        """ self explanatory """
        if is_correct:
            self.answers["correct_answers"][question_index] = answer
        else:
            self.answers["wrong_answers"][question_index] = answer

    def prompt_score(self, count):
        """ self explanatory """
        print(f"Your score is {self.score}/{count}\n")

    def prompt_answers(self):
        """ code smell that HAS to get refactored """  
        print("✅ Correct Answers:\n")
        for answer in self.answers["correct_answers"]:
            print(f"{answer}\n")

        print("❌ Wrong Answers:\n")
        for answer in self.answers["wrong_answers"]:
            print(f"{answer}\n")

