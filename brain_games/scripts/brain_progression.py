#!/usr/bin/env python3

from brain_games import engine


def logic_game():
    engine.greet()
    engine.welcome_user()
    rule_game = 'What number is missing in the progression?'
    print(rule_game)
    count = 1
    while count <= 3:
        lst = list(range(engine.random_number(2, 10),
                   engine.random_number(120, 150),
                   engine.random_number(3, 10)))
        result = lst[engine.random_number(0, 10)]
        for i, n in enumerate(lst):
            if n == result:
                lst[i] = '..'
        res = ' '.join(str(el) for el in lst[:11])
        print(f'Question: {res}')
        if engine.comparing_response(result) is True:
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
