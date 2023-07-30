from random import randint
from ..engine import run_game


DESCRIPTION =\
    """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_game_data(start_num=1, end_num=99):
    number = randint(start_num, end_num)
    correct_answer = is_prime(number)
    correct_answer = correct_answer * 'yes' + (not correct_answer) * 'no'

    return number, correct_answer


def run_prime():
    return run_game(generate_game_data, DESCRIPTION)
