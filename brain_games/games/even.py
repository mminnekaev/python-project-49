from random import randint
from ..engine import run_game


DESCRIPTION = """Answer "yes" if the number is even, otherwise answer "no"."""


def generate_game_data(start_num=1, end_num=99):
    """Generates random integer and correct answer"""

    num = randint(start_num, end_num)
    if num % 2 == 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return num, correct_answer


def run_even():
    return run_game(generate_game_data, DESCRIPTION)
