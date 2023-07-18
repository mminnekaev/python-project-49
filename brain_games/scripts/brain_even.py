#!/usr/bin/env python3
from random import randint
from ..cli import welcome_user

def check_even_number(name, n=3, start_num=1, end_num=99):
    """Generates random integer n times and check answers"""

    print("""Answer "yes" if the number is even, otherwise answer "no".""")

    while n > 0:
        num = randint(start_num, end_num)
        print(f"Question: {num}")
        answer = input("Your answer: ")
        # print(f"Your answer: {answer}")

        if (num % 2 == 1 and answer == 'yes'):
            print("""'yes' is wrong answer ;(. Correct answer was 'no'.""")
            print(f"""Let's try again, {name}!""")
            return None
        elif (num % 2 == 0 and answer == 'no'):
            print("""'no' is wrong answer ;(. Correct answer was 'yes'.""")
            print(f"""Let's try again, {name}!""")
            return None
        else:
            print("Correct!")
            n -= 1

    print(f"Congratulations, {name}!")

def main():
    name = welcome_user()
    check_even_number(name)

if __name__ == "__main__":
    main()