#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import gcd


def main():
    name = welcome_user()
    gcd.check_gcd(name)


if __name__ == "__main__":
    main()
