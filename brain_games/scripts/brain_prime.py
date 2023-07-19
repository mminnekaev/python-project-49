#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import prime


def main():
    name = welcome_user()
    prime.check_prime(name)


if __name__ == "__main__":
    main()
