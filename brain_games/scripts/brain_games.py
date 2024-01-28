#!/usr/bin/env python3

from brain_games import cli

def greet():
    print(f'Welcome to the Brain Games!')

def main():
    greet()
    cli.welcome_user()

if __name__ == '__main__':
    main()
