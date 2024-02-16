#!/usr/bin/env python3

import operator
import random
from brain_games import engine


def logic_game():
    engine.greet()
    engine.welcome_user()
    rule_game = 'What is the result of the expression?'
    print(rule_game)
    count = 1
    while count <= 3:
        rand_num_1 = engine.random_number(1, 10)
        rand_num_2 = engine.random_number(1, 10)
        random_sign = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        choice_sign = random.choice(list(random_sign.keys()))
        result_exp = random_sign.get(choice_sign)(rand_num_1, rand_num_2)
        expression = f'{rand_num_1} {choice_sign} {rand_num_2}'
        print(f'Question: {expression}')
        if engine.comparing_response(result_exp) is True:
            count += 1
            if count > 3:
                engine.victory()
                break
        else:
            break


def main():
    logic_game()


if __name__ == '__main__':
    main()
