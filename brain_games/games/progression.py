import random


CONDITION = 'What number is missing in the progression?'


def get_parameter_game():
    start_lst = random.randint(2, 10)
    step_lst = random.randint(5, 10)
    stop_lst = 100
    lst = [i for i in range(start_lst, stop_lst, step_lst)]

    result = lst[random.randint(0, 10)]

    for i, n in enumerate(lst):
        if n == result:
            lst[i] = '..'
    expression = ' '.join(str(x) for x in lst[:11])

    return expression, result
