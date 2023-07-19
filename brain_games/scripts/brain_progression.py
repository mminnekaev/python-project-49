#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import progression


def main():
    name = welcome_user()
    progression.check_progression(name)


if __name__ == "__main__":
    main()
