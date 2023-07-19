#!/usr/bin/env python3
from random import randint


def check_even_number(name, n=3, start_num=1, end_num=99):
    """Generates random integer n times and check answers"""

    print("""Answer "yes" if the number is even, otherwise answer "no".""")

    while n > 0:
        num = randint(start_num, end_num)
        if num % 2 == 1:
            correct_answer = 'no'
        elif num % 2 == 0:
            correct_answer = 'yes'

        print(f"Question: {num}")
        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            n -= 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
            print(f"""Let's try again, {name}!""")
            return None

    print(f"Congratulations, {name}!")
