#!/bin/env python3


"""Title"""


__author__ = "rodrig_a"


def build_string(question, options, is_menu=False):
    """
    i've implemented it as functionnal programming because I don't
    need any string creator class
    """
    question_string = question
    for i in options:
        if is_menu:
            question_string += f"\n{options.index(i) + 1}. {i}"
        else:
            question_string += f"\n{options.index(i) + 1}. {i}" 
    return question_string + "\n"


def translate_int_to_answer(input, options):
    """ 
    i'm returning an answer from an int 
    because the player chooses an answer via integers
    and the answer check is done via the answer string
    """
    return options[int(input) - 1]