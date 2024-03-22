import random


CONDITION = 'What number is missing in the progression?'


def describes_the_logic():
    lst = list(range(random.randint(2, 10),
               random.randint(120, 150),
               random.randint(3, 10)))
    result = lst[random.randint(0, 10)]

    for i, n in enumerate(lst):
        if n == result:
            lst[i] = '..'
    expression = ' '.join(str(el) for el in lst[:11])
    return (expression, result)
