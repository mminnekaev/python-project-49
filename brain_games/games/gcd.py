#!/usr/bin/env python3
from random import randint


def find_gcd(num_1: int, num_2: int):
    """Return the greatest common divisor of two integers"""
    min_num = max(num_1, num_2)
    for i in range(1, min_num + 1):
        if ((num_1 % i == 0) and (num_2 % i == 0)):
            gcd = i

    return gcd


def check_gcd(start_num=1, end_num=99):
    """Generates pair of numbers and greatest common divisor"""

    num_1 = randint(start_num, end_num)
    num_2 = randint(start_num, end_num)
    correct_answer = str(find_gcd(num_1, num_2))

    return str(num_1) + ' ' + str(num_2), correct_answer
