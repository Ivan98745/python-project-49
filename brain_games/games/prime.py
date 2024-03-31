import random


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_parameter_game():
    rand_num = random.randint(-10, 100)
    expression = f'{rand_num}'
    result = 'yes' if is_prime(rand_num) else 'no'
    return expression, result


def is_prime(numb):
    i = numb
    while i > 2:
        if numb % (i - 1) != 0:
            i -= 1
        else:
            break
    return i == 2
