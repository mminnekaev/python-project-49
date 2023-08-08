from random import randint


DESCRIPTION = """Find the greatest common divisor of given numbers."""


def find_gcd(num_1: int, num_2: int):
    """Return the greatest common divisor of two integers"""
    min_num = max(num_1, num_2)
    for i in range(1, min_num + 1):
        if ((num_1 % i == 0) and (num_2 % i == 0)):
            gcd = i

    return gcd


def generate_game_data():
    """Generates pair of numbers and greatest common divisor"""

    num_1 = randint(1, 99)
    num_2 = randint(1, 99)
    correct_answer = str(find_gcd(num_1, num_2))

    return f"{num_1} {num_2}", correct_answer
