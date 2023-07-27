#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import engine, prime


def main():
    name = welcome_user()
    print("""Answer "yes" if given number is prime. Otherwise answer "no".""")
    N = 3
    questions, correct_answers = zip(*[prime.check_prime() for i in range(N)])
    engine.engine(player_name=name, questions=questions,
                  correct_answers=correct_answers, n=N)


if __name__ == "__main__":
    main()
