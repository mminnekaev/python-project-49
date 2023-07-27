#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import engine, progression


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    N = 3
    questions, correct_answers = zip(
        *[progression.check_progression() for i in range(N)]
    )
    engine.engine(player_name=name, questions=questions,
                  correct_answers=correct_answers, n=N)


if __name__ == "__main__":
    main()
