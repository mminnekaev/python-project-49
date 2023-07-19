#!/usr/bin/env python3
from random import randint

def generate_progression(start_num, step, length):
    progression = [i for i in range(start_num, start_num + length * step, step)]
    return progression

def check_progression(name, length=10, n=3):
    """Checks missing number in progression"""

    while n > 0:
        # define progression parameters
        start_num = randint(1,99)
        step = randint(1, 10)
        progression = generate_progression(start_num, step, length)

        # modifying progression by dropping random element
        progression_int = list(map(lambda x: str(x), progression))
        missing_elem_num = randint(1, len(progression) - 1)
        progression_with_missing_num = ' '.join(progression_int[: missing_elem_num]) \
                                       + ' .. ' \
                                       + ' '.join(progression_int[missing_elem_num + 1 :])

        correct_answer = progression_int[missing_elem_num]

        print("What number is missing in the progression?")
        print(f"Question: {progression_with_missing_num}")

        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            n -= 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
            print(f"""Let's try again, {name}!""")
            return None

    print(f"Congratulations, {name}!")
