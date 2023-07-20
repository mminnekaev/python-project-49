#!/usr/bin/env python3
from random import randint
from .check_answer import check_answer


def is_prime(number):
    if number <= 3:
        return True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def check_prime(name, n=3, start_num=1, end_num=99):

    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")

    while n > 0:
        number = randint(start_num, end_num)
        correct_answer = is_prime(number)
        correct_answer = correct_answer * 'yes' + (not correct_answer) * 'no'
        print(f"Question: {number}")
        answer = input("Your answer: ")

        if check_answer(answer, correct_answer, name) is False:
            return None
        else:
            n -= 1
