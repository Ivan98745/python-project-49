import random


CONDITION = 'Find the greatest common divisor of given numbers.'


def get_question_nad_answer():
    rand_num_1 = random.randint(1, 100)
    rand_num_2 = random.randint(1, 100)
    expression = f'{rand_num_1} {rand_num_2}'

    result = gets_smallest_divisor(rand_num_1, rand_num_2)
    return expression, result


def gets_smallest_divisor(numb_1, numb_2):
    while numb_1 != numb_2:
        if numb_1 > numb_2:
            numb_1 = numb_1 - numb_2
        else:
            numb_2 = numb_2 - numb_1
    return numb_2
