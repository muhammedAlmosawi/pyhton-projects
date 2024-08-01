import random
from MathQuiz import *


def random_generator():
    first_number = random.randint(MIN_OPERAND, MAX_OPERAND)
    second_number = random.randint(MIN_OPERAND, MAX_OPERAND)
    operand = random.choice(OPERATORS)
    full_expression = str(first_number) + " " + operand + " " + str(second_number)
    answer = eval(full_expression)
    return full_expression, answer

