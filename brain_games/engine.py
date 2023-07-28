#!/usr/bin/env python3
from .cli import welcome_user


def run_game(questions, correct_answers, n, desc):
    player_name = welcome_user()
    print(desc)

    while n > 0:
        question = questions[n - 1]
        correct_answer = correct_answers[n - 1]
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
