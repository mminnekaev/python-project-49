#!/usr/bin/env python3
from ..games import prime
from .. import engine


N = 3


def main():
    questions, correct_answers = zip(*[prime.check_prime() for i in range(N)])
    engine.run_game(questions=questions, correct_answers=correct_answers,
                    n=N, desc=prime.DESCRIPTION)


if __name__ == "__main__":
    main()
