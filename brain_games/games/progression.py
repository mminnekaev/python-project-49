from random import randint


DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start_num, step, length):
    return [i for i in range(start_num, start_num + length * step, step)]


def generate_game_data(length=10):
    """Generates progression and missing number in it"""

    # define progression parameters
    start_num = randint(1, 99)
    step = randint(1, 10)
    progression_items = generate_progression(start_num, step, length)
    progression_items = list(map(str, progression_items))

    # modifying progression by dropping random element
    missing_elem_num = randint(1, len(progression_items) - 1)
    correct_answer = progression_items[missing_elem_num]

    progression_items[missing_elem_num] = '..'
    progression_with_missing_num = ' '.join(progression_items)

    return progression_with_missing_num, correct_answer
