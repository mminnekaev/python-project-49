#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import engine, even


def main():
    name = welcome_user()
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    N = 3
    questions, correct_answers = zip(
        *[even.check_even_number() for i in range(N)]
    )
    engine.engine(player_name=name, questions=questions,
                  correct_answers=correct_answers, n=N)


if __name__ == "__main__":
    main()
