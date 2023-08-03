from random import randint
import math


DESCRIPTION =\
    """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def generate_game_data(start_num=1, end_num=99):
    number = randint(start_num, end_num)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return number, correct_answer
