#!/bin/env python3


"""Quiz"""

import time


from utils import build_string
from quiz import Question
from player_progression import PlayerProgression


__author__ = "rodrig_a"


def main():
    """ starts quiz main loop, asks for starting game, quitting """
    cond = choice_menu()
    question_index = 0
    while True:

        player_progression = PlayerProgression()
        # question = Question(
            # {
                # "question": "Quelle est la sortie de print(type(3)) ?",
                # "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"],
                # "answer": "<class 'int'>"
            # }
        # )
        question = Quiz.get_question_by_index(question_index)
        
        question_index += 1
        answer = question.ask_question_get_answer(question)
        if question.is_correct_answer(answer):
            question.prompt_correct_answer()
            player_progression.increment_score()
            print(f"Your score is {player_progression.score}")
            player_progression.add_answer_to_progression(answer, 1, True)
            print(f"Here are your correct answers {player_progression.answers['correct_answers']}")
        else:
            question.prompt_wrong_answer()
            player_progression.add_answer_to_progression(answer)
        break


def choice_menu():
    """ ask for starting game, see results or quit """
    menu_string = build_string("Welcome to Quizzified :", ["Play", "See results", "Quit"], True)
    user_choice = input(menu_string)
    return True


def initialize_player_progression():
    return {
        "player_name": "",
        "score": 0,
        "correct_answers": {},
        "wrong_answers": {}
    }
        

main()



