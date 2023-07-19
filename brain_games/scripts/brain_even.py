#!/usr/bin/env python3
from random import randint
from ..cli import welcome_user
from ..games import even

def main():
    name = welcome_user()
    even.check_even_number(name)

if __name__ == "__main__":
    main()