#!/usr/bin/env python3
from random import randint, choice

def check_calc(name, n=3, start_num=1, end_num=99):
    """Generates random operations with integers n times and check answers"""

    print("""What is the result of the expression?""")

    while n > 0:
        num_1 = randint(start_num, end_num)
        num_2 = randint(start_num, end_num)
        operation = choice(['+', '-', '*'])

        if operation == '+':
            correct_answer = num_1 + num_2
        elif operation == '-':
            correct_answer = num_1 - num_2
        elif operation == '*':
            correct_answer = num_1 * num_2

        print(f"Question: {num_1} {operation} {num_2}")
        answer = input(f"Your answer: ")

        if answer == str(correct_answer):
            print("Correct!")
            n -= 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
            print(f"Let's try again, {name}!")
            return None

    print(f"Congratulations, {name}!")
