#!/usr/bin/env python3
from ..games import gcd
from .. import engine


N = 3


def main():
    questions, correct_answers = zip(*[gcd.check_gcd() for i in range(N)])
    engine.run_game(questions=questions, correct_answers=correct_answers,
                    n=N, desc=gcd.DESCRIPTION)


if __name__ == "__main__":
    main()
