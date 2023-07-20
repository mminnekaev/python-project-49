#!/usr/bin/env python3
from random import randint, choice
from .check_answer import check_answer


def check_calc(name, n=3, start_num=1, end_num=99):
    """Generates random operations with integers n times and check answers"""

    print("""What is the result of the expression?""")

    while n > 0:
        num_1 = randint(start_num, end_num)
        num_2 = randint(start_num, end_num)
        operation = choice(['+', '-', '*'])

        if operation == '+':
            correct_answer = str(num_1 + num_2)
        elif operation == '-':
            correct_answer = str(num_1 - num_2)
        elif operation == '*':
            correct_answer = str(num_1 * num_2)

        print(f"Question: {num_1} {operation} {num_2}")
        answer = input("Your answer: ")

        if check_answer(answer, correct_answer, name) is False:
            return None
        else:
            n -= 1

    print(f"Congratulations, {name}!")
