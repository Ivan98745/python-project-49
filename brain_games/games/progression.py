#!/usr/bin/env python3


import random


def logic_game():
    condition = 'What number is missing in the progression?'
    lst = list(range(random.randint(2, 10),
               random.randint(120, 150),
               random.randint(3, 10)))
    result = lst[random.randint(0, 10)]
    for i, n in enumerate(lst):
        if n == result:
            lst[i] = '..'
    expression = ' '.join(str(el) for el in lst[:11])
    return (expression, result, condition)
