import random


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic_game():
    rand_num = random.randint(1, 100)
    if rand_num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    expression = f'{rand_num}'
    return (expression, result)
