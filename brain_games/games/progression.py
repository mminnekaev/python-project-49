#!/usr/bin/env python3
from random import randint


def generate_progression(start_num, step, length):
    progression = [i for i in range(start_num, start_num + length * step, step)]
    return progression


def check_progression(length=10, n=3):
    """Generates progression and missing number in it"""

    # define progression parameters
    start_num = randint(1, 99)
    step = randint(1, 10)
    progression = generate_progression(start_num, step, length)

    # modifying progression by dropping random element
    progression_int = list(map(lambda x: str(x), progression))
    missing_elem_num = randint(1, len(progression) - 1)
    progression_with_missing_num = \
        ' '.join(progression_int[: missing_elem_num]) \
        + ' .. ' \
        + ' '.join(progression_int[missing_elem_num + 1:])

    correct_answer = progression_int[missing_elem_num]

    return progression_with_missing_num, correct_answer
