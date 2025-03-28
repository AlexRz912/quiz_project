#!/bin/env python3


"""Title"""

import os
import time

from datetime import date


__author__ = "rodrig_a"


def build_string(question, options):
    """
    i've implemented it as functionnal programming because I don't
    need any string creator class
    """
    delimiter = "------------------------------------------------------------------------------------"
    question_string = delimiter + "\n\n" + question + "\n\n" + delimiter + "\n"
    for i in options:
        question_string += f"\n{options.index(i) + 1}. {i}" 
    return "\n" + question_string + "\n\n\n"


def translate_int_to_answer(input, options):
    """ 
    i'm returning an answer from an int 
    because the player chooses an answer via numbers
    and the answer check is done via the answer string
    """
    return options[int(input) - 1]


def user_wants_to_save():
    """
    Self explanatory
    """
    while True:
        try:
            wish = input("Do you want to save your score (Y/n)\n").lower()
            if wish == "y":
                return True
            elif wish == "n":
                return False
            else:
                print("Please provide a correct input as mentionned: y or n")
                continue
        except Exception as e:
            print(f"Unexpected error : {e}")
            continue

def get_date():
    """ pure util as they come lol """
    return date.today().strftime("%Y-%m-%d")

def get_percentage_as_int(value, max_value):
    """ Self explanatory """
    return int(value / max_value * 100)

def clear_terminal():
    """ pure util as they come lol """
    os.system('cls' if os.name == 'nt' else 'clear')

def give_time_to_read(read_time):
    """ pure util as they come lol """
    time.sleep(read_time)