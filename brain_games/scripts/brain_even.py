#!/usr/bin/env python3


import prompt
import random


def greet():
    greeting = 'Welcome to the Brain Games!'
    print(f'{greeting}')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    return print('Hello, ' + name + '!')


def game_conditions():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(f'{condition}')


def logic_game():
    negative_result = ("'yes' is wrong answer ;(. Correct answer was 'no'."
                       "\nLet's try again, ")
    i = 1
    while i <= 3:
        random_numb = random.randint(1, 500)
        print('Question: ' + str(random_numb))
        question = prompt.string('Your answer: ')
        if (random_numb % 2 == 0 and question == 'yes'
                or random_numb % 2 != 0 and question == 'no'):
            print('Correct!')
            i += 1
        else:
            print(f'{negative_result}{name}!')
            break
        if i > 3:
            print(f'Congratulations, {name}!')


def main():
    greet()
    welcome_user()
    game_conditions()
    logic_game()


if __name__ == '__main__':
    main()
