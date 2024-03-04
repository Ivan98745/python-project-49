import random


def logic_game():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    rand_num = random.randint(3, 100)
    expression = f'{rand_num}'
    i = rand_num
    while i > 2:
        if rand_num % (i - 1) != 0:
            i -= 1
            result = 'yes'
        else:
            result = 'no'
            break
    return (expression, result, condition)
