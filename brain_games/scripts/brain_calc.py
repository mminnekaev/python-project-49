#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import engine, calc


def main():
    name = welcome_user()
    print("""What is the result of the expression?""")
    N = 3
    questions, correct_answers = zip(*[calc.check_calc() for i in range(N)])
    engine.engine(player_name=name, questions=questions,
                  correct_answers=correct_answers, n=N)


if __name__ == "__main__":
    main()
