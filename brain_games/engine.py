#!/usr/bin/env python3
import prompt
from .games import calc, even, gcd, prime, progression


def generate_game_data(game_name):
    """Checks game_name and returns question and correct_answer"""

    if game_name == 'calc':
        question, correct_answer = calc.check_calc()
    elif game_name == 'even':
        question, correct_answer = even.check_even_number()
    elif game_name == 'gcd':
        question, correct_answer = gcd.check_gcd()
    elif game_name == 'prime':
        question, correct_answer = prime.check_prime()
    elif game_name == 'progression':
        question, correct_answer = progression.check_progression()
    else:
        return None

    return question, correct_answer


def choose_description(game_name):
    """Checks game_name and returns question and correct_answer"""

    if game_name == 'calc':
        desc = calc.DESCRIPTION
    elif game_name == 'even':
        desc = even.DESCRIPTION
    elif game_name == 'gcd':
        desc = gcd.DESCRIPTION
    elif game_name == 'prime':
        desc = prime.DESCRIPTION
    elif game_name == 'progression':
        desc = progression.DESCRIPTION
    else:
        desc = None

    return desc


def run_game(game_name, n=3):
    # Greeting
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(choose_description(game_name=game_name))

    # Answering questions and checking answers
    while n > 0:
        question, correct_answer = generate_game_data(game_name=game_name)
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            n -= 1
        else:
            text = " is wrong answer ;(. Correct answer was "
            print(f"""'{answer}'{text}'{correct_answer}'.""")
            print(f"Let's try again, {player_name}!")
            return

    print(f"Congratulations, {player_name}!")
