#!/usr/bin/env python3


import prompt
import random
import operator


def greet():
    greeting = 'Welcome to the Brain Games!'
    print(f'{greeting}')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    return print('Hello, ' + name + '!')


def game_conditions():
    condition = 'What is the result of the expression?'
    print(f'{condition}')

def logic_game():
    i = 1
    while i <= 3:
        random_numb1, random_numb2 = random.randint(1, 10), random.randint(1, 10)
        random_sign = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        op = random.choice(list(random_sign.keys()))
        result = random_sign.get(op)(random_numb1, random_numb2)
        expression = f'{random_numb1} {op} {random_numb2}'
        print('Question: ' + str(expression))
        question = prompt.string('Your answer: ')
        if str(result) == question:
            print('Correct!')
            i += 1
        else:
            negative_result = (f'\'{question}\' is wrong answer ;(. Correct answer was \'{result}\'.'
                              "\nLet's try again, ")
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
