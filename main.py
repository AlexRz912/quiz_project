#!/bin/env python3


"""Quizzified"""


import json

from utils import build_string
from utils import user_wants_to_save
from utils import get_date
from utils import get_percentage_as_int
from utils import clear_terminal
from utils import give_time_to_read

from player_progression import PlayerProgression
from quiz import Quiz
from user import User


__author__ = "rodrig_a"


def main():
    """ starts main loop, three possibilites """
    while True:
        clear_terminal()
        user_choice = choice_menu()
        if user_choice == '3':

            clear_terminal()
            print("👋 Byebye !")
            give_time_to_read(1)
            clear_terminal()
            return

        if user_choice == '2':
            clear_terminal()
            problem = load_results_if_no_error()
            if not problem:
                continue
            print("Something wrong occured, please see above notice before contacting us (RTFM)")
            return
        if user_choice == '1':
            index = 0
            progression = PlayerProgression()
            quiz = Quiz()
            question_count = question_loop(index, progression, quiz)
            game_ended(progression, question_count)
    

def question_loop(question_index, player_progression, quiz):
    """quiz question loop"""
    while True:
        clear_terminal()
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

        give_time_to_read(2)
        if question_index >= quiz.get_questions_count():
            clear_terminal()
            return question_index


def choice_menu():
    """ ask for starting game, see results or quit """
    menu_string = build_string("Welcome to Quizzified :", ["Play", "See results", "Quit"])
    user_choice = input(menu_string)
    return user_choice
        
def game_ended(player_progression, question_count):

    player_progression.prompt_score(question_count)
    player_progression.prompt_answers()

    if user_wants_to_save():

        nickname = input("Choose a nickname :\n")
        user = User(
            nickname, 
            get_percentage_as_int(player_progression.score, question_count), 
            get_date()
        )
        user.users_data = user.json_load_all_users()
        if not user.users_exists():
            user.json_save_user()
        user.json_save_score()

def load_results_if_no_error():
    try:
        with open("data/utilisateurs.json", "r", encoding="utf-8") as user_results_file:
            user_results = json.load(user_results_file)
        for username, user in user_results.items():  
            prompt_results_for_user(username, user)
        input("press enter to continue :\n")
        return False

    except KeyError:
        print("Error encountered while trying to print, data/utilisateurs.json entries are not valid")
        return True
    except FileNotFoundError:
        print("Error encountered while trying to load data/utilisateurs.json. File doesn't exist.")
        return True

def prompt_results_for_user(username, user):
    print(f"Scores for {username}:\n\n")

    print(f"{len(user['scores'])} attempts :\n")
    for i in user["scores"]:
        prompt_result(i)
    print("\n")

def prompt_result(score_record):
    for i, v in score_record.items():
        print(f"{i}: {v}")

main()
