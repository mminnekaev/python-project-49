from random import randint


DESCRIPTION = """Answer "yes" if the number is even, otherwise answer "no"."""


def generate_game_data():
    """Generates random integer and correct answer"""

    num = randint(1, 99)
    if num % 2 == 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return num, correct_answer
