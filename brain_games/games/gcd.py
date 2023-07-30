from random import randint
from ..engine import run_game


DESCRIPTION = """Find the greatest common divisor of given numbers."""


def find_gcd(num_1: int, num_2: int):
    """Return the greatest common divisor of two integers"""
    min_num = max(num_1, num_2)
    for i in range(1, min_num + 1):
        if ((num_1 % i == 0) and (num_2 % i == 0)):
            gcd = i

    return gcd


def generate_game_data(start_num=1, end_num=99):
    """Generates pair of numbers and greatest common divisor"""

    num_1 = randint(start_num, end_num)
    num_2 = randint(start_num, end_num)
    correct_answer = str(find_gcd(num_1, num_2))

    return f"{num_1} {num_2}", correct_answer


def run_gcd():
    return run_game(generate_game_data, DESCRIPTION)
