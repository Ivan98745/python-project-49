import operator
import random


CONDITION = 'What is the result of the expression?'


def describes_the_logic():
    rand_num_1 = random.randint(1, 10)
    rand_num_2 = random.randint(1, 10)

    random_sign = [('+', operator.add),
                   ('-', operator.sub),
                   ('*', operator.mul)]
    choice_sign = random.choice(random_sign)
    result_exp = (choice_sign[1])(rand_num_1, rand_num_2)
    expression = f'{rand_num_1} {choice_sign[0]} {rand_num_2}'
    return (expression, result_exp)
