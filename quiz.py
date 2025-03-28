#!/bin/env python3


"""Quiz Classes"""


import json
import random


import utils


__author__ = "rodrig_a"


class Quiz:
    """
    I've created a quiz class to load questions and generate the quiz outside of the question loop 
    and handle anything that is related to all questions, or return the correct question in relation
    to the loop index in get_question_by_index()
    """

    def __init__(self):
        """I've decided to delegate the json handling and the question generation"""
        self.data = self.load_questions()
        self.questions = self.generate_questions()


    def load_questions(self):
        """json load, nothing much to say about it"""
        with open("data/questions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
        
    def generate_questions(self):
        """calls min_five_question, because I'm delegating the shit code to a sub method"""
        return self.min_five_questions([])

    def min_five_questions(self, questions):
        """
        Every question in the loaded file have a 50 % chance of appearing, until the for loops ends,
        then only do they get more chance to appear if the length of the quiz is inferior to 5 
        """
        while True:
            for i in self.data:
                if random.randint(0, 1):
                    questions.append(i) 
            if len(questions) < 5:
                continue
            return questions

    def get_question_by_index(self, index):
        return Question(self.questions[index])

    def get_questions_count(self):
        return len(self.questions)

    

class Question:
    """I've created this class"""
    def __init__(self, question: dict):
        """"""
        self.question = question["question"]
        self.options = question["options"]
        self.answer = question["reponse"]


    def is_correct_answer(self, answer):
        """
        called as a condition in main, to check if the answer is correct, 
        implemented here, because it is this class that verifies if the question is correct
        """
        return self.answer == answer


    def prompt_wrong_answer(self):
        """self explanatory"""
        print(f"Wrong, right answer was {self.answer}")


    def prompt_correct_answer(self):
        """self explanatory"""
        print(f"Good job! this is correct")


    def ask_question_get_answer(self, question):
        """ self explanatory """
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