#!/bin/env python3


"""Quizzified"""

import time


from utils import build_string
from utils import user_wants_to_save

from player_progression import PlayerProgression
from quiz import Quiz
from user import User


__author__ = "rodrig_a"


def main():
    """ starts main loop, three possibilites """
    while True:
        user_choice = choice_menu()
        if user_choice == '3':
            print("Byebye !")
            return
        elif user_choice == '2':
            raise NotImplementedError
        elif user_choice == '1':
            index = 0
            progression = PlayerProgression()
            quiz = Quiz()
            question_count = question_loop(index, progression, quiz)
            game_ended(progression, question_count)
    

def question_loop(question_index, player_progression, quiz):
    """quiz question loop"""
    while True:
        question = quiz.get_question_by_index(question_index)
        question_index += 1
        answer = question.ask_question_get_answer(question)

        if question.is_correct_answer(answer):
            question.prompt_correct_answer()
            player_progression.increment_score()
            player_progression.add_answer_to_progression(answer, question_index, True)
        else:
            question.prompt_wrong_answer()
            player_progression.add_answer_to_progression(answer, question_index)

        if question_index >= quiz.get_questions_count():
            return question_index


def choice_menu():
    """ ask for starting game, see results or quit """
    menu_string = build_string("Welcome to Quizzified :", ["Play", "See results", "Quit"], True)
    user_choice = input(menu_string)
    return user_choice
        
def game_ended(player_progression, question_count):
    player_progression.prompt_score(question_count)
    player_progression.prompt_answers()
    if user_wants_to_save():
        nickname = input("Choose a nickname :\n")
        user = User(nickname)
main()