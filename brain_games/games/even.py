import random


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_nad_answer():
    rand_num = random.randint(1, 100)
    result = 'yes' if rand_num % 2 == 0 else 'no'

    return str(rand_num), result
