#!/usr/bin/env python3
from ..games import calc
from .. import engine


N = 3


def main():
    questions, correct_answers = zip(*[calc.check_calc() for i in range(N)])
    engine.run_game(questions=questions, correct_answers=correct_answers,
                    n=N, desc=calc.DESCRIPTION)


if __name__ == "__main__":
    main()
