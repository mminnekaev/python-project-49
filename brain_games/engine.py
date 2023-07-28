#!/usr/bin/env python3
import prompt
from .games import calc, even, gcd, prime, progression


def generate_game_data(game_name):
    """Checks game_name and returns question and correct_answer"""

    if game_name == 'calc':
        return calc.check_calc()
    elif game_name == 'even':
        return even.check_even_number()
    elif game_name == 'gcd':
        return gcd.check_gcd()
    elif game_name == 'prime':
        return prime.check_prime()
    elif game_name == 'progression':
        return progression.check_progression()
    else:
        return None


def choose_description(game_name):
    """Checks game_name and returns question and correct_answer"""

    if game_name == 'calc':
        return calc.DESCRIPTION
    elif game_name == 'even':
        return even.DESCRIPTION
    elif game_name == 'gcd':
        return gcd.DESCRIPTION
    elif game_name == 'prime':
        return prime.DESCRIPTION
    elif game_name == 'progression':
        return progression.DESCRIPTION
    else:
        return None


def run_game(game_name, n=3):
    # Greeting
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
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
