#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import engine, gcd


def main():
    name = welcome_user()
    print("""Find the greatest common divisor of given numbers.""")
    N = 3
    questions, correct_answers = zip(*[gcd.check_gcd() for i in range(N)])
    engine.engine(player_name=name, questions=questions,
                  correct_answers=correct_answers, n=N)


if __name__ == "__main__":
    main()
