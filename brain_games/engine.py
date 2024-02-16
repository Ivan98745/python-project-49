import prompt
import random


def greet():
    greeting = 'Welcome to the Brain Games!'
    print(f'{greeting}')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    return print('Hello, ' + name + '!')


def random_number():
    number = random.randint(1, 10)
    return number


def negative_result():
    part_1 = 'is wrong answer ;(. Correct answer was'
    part_2 = "\nLet's try again, "
    return (part_1, part_2)


def comparing_response(answer):
    neg_res = negative_result()
    question = prompt.string('Your answer: ')
    if str(answer) == question:
        print('Correct!')
        return True
    else:
        print(f"\'{question}\' {neg_res[0]} \'{answer}\'.{neg_res[1]}{name}!")
        return False


def victory():
    print(f'Congratulations, {name}!')
