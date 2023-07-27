#!/usr/bin/env python3
from random import randint


def check_even_number(start_num=1, end_num=99):
    """Generates random integer and correct answer"""

    num = randint(start_num, end_num)
    if num % 2 == 1:
        correct_answer = 'no'
    elif num % 2 == 0:
        correct_answer = 'yes'

    return num, correct_answer
