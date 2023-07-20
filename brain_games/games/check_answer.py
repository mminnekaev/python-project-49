#!/usr/bin/env python3
def check_answer(answer, correct_answer, name):
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
        print(f"Let's try again, {name}!")
        return False
