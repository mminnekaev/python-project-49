from random import randint, choice


DESCRIPTION = """What is the result of the expression?"""


def generate_game_data(start_num=1, end_num=99):
    """Generates random operations with integers and check answers"""

    num_1 = randint(start_num, end_num)
    num_2 = randint(start_num, end_num)
    operation = choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2

    correct_answer = str(correct_answer)

    return f"{num_1} {operation} {num_2}", correct_answer
