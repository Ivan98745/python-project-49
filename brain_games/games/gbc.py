#!/usr/bin/env python3


import random


def logic_game():
    condition = 'Find the greatest common divisor of given numbers.'
    rand_num_1 = random.randint(1, 100)
    rand_num_2 = random.randint(1, 100)
    expression = f'{rand_num_1} {rand_num_2}'
    while rand_num_1 != rand_num_2:
        if rand_num_1 > rand_num_2:
            rand_num_1 = rand_num_1 - rand_num_2
        else:
            rand_num_2 = rand_num_2 - rand_num_1
    result = rand_num_2
    return (expression, result, condition)
