#!/usr/bin/env python3
from random import randint


def find_gcd(num_1: int, num_2: int):
    """Return the greatest common divisor of two integers"""
    min_num = max(num_1, num_2)
    for i in range(1, min_num + 1):
        if ((num_1 % i == 0) and (num_2 % i == 0)):
            gcd = i

    return gcd


def check_gcd(name, n=3, start_num=1, end_num=99):
    """Checks greatest common divisor"""

    print("""Find the greatest common divisor of given numbers.""")

    while n > 0:
        num_1 = randint(start_num, end_num)
        num_2 = randint(start_num, end_num)
        correct_answer = find_gcd(num_1, num_2)

        print(f"Question: {num_1} {num_2}")
        answer = input("Your answer: ")

        if answer == str(correct_answer):
            print("Correct!")
            n -= 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
            print(f"""Let's try again, {name}!""")
            return None

    print(f"Congratulations, {name}!")
