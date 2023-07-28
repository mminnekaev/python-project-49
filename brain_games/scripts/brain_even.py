#!/usr/bin/env python3
from ..games import even
from .. import engine


N = 3


def main():
    questions, correct_answers = zip(
        *[even.check_even_number() for i in range(N)]
    )
    engine.run_game(questions=questions, correct_answers=correct_answers,
                    n=N, desc=even.DESCRIPTION)


if __name__ == "__main__":
    main()
