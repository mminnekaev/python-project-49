#!/usr/bin/env python3
from ..games import progression
from .. import engine


N = 3


def main():
    questions, correct_answers = zip(
        *[progression.check_progression() for i in range(N)]
    )
    engine.run_game(questions=questions, correct_answers=correct_answers,
                    n=N, desc=progression.DESCRIPTION)


if __name__ == "__main__":
    main()
