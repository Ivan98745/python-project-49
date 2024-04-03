import random


CONDITION = 'What number is missing in the progression?'


def get_question_nad_answer():
    start = random.randint(2, 10)
    step = random.randint(5, 10)
    length = 10
    stop = start + (step * length)
    progression = list(range(start, stop, step))

    result = random.randrange(start, stop, step)
    index_result = progression.index(result)

    progression[index_result] = '..'
    expression = ' '.join(str(el) for el in progression)

    return expression, result
