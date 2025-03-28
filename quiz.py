#!/bin/env python3


"""Title"""


import json
import random


import utils


__author__ = "rodrig_a"


class Quiz:
    def __init__(self):
        self.data = load_questions()
        self.questions = generate_quiz()

    def load_questions():
        return

    def generate_questions():
        return

    def get_question_by_index():
        return

    

class Question:
    def __init__(self, question: dict):
        self.question = question["question"]
        self.options = question["options"]
        self.answer = question["answer"]


    def is_correct_answer(self, answer):
        return self.answer == answer


    def prompt_wrong_answer(self):
        right_answer = self.answer
        print(f"Wrong, right answer was {right_answer}")


    def prompt_correct_answer(self):
        print(f"Good job! this is correct")


    def ask_question_get_answer(self, question):
        """ to refactor into question Class """
        while True: 

            ask_for_answer_string = utils.build_string(self.question, self.options)

            answer_as_int = input(ask_for_answer_string)
            if not answer_as_int.isdigit():
                print("Please provide a corresponding number to possible answers.")
                continue
            if int(answer_as_int) not in range(1, len(self.options) + 1):
                print("Please provide a corresponding number to possible answers")
                continue

            return utils.translate_int_to_answer(answer_as_int, self.options)