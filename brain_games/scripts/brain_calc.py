#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import calc


def main():
    name = welcome_user()
    calc.check_calc(name)


if __name__ == "__main__":
    main()
