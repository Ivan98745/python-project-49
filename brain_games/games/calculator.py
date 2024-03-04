#!/usr/bin/env python3


import operator
import random


def logic_game():
    condition = 'What is the result of the expression?'
    rand_num_1 = random.randint(1, 10)
    rand_num_2 = random.randint(1, 10)
    random_sign = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    choice_sign = random.choice(list(random_sign.keys()))
    result_exp = random_sign.get(choice_sign)(rand_num_1, rand_num_2)
    expression = f'{rand_num_1} {choice_sign} {rand_num_2}'
    return (expression, result_exp, condition)
