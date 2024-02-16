#!/usr/bin/env python3

from brain_games import engine


def logic_game():
    engine.greet()
    engine.welcome_user()
    rule_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(rule_game)
    count = 1
    while count <= 3:
        rand_num = engine.random_number()
        print(f'Question: {rand_num}')
        if rand_num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
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
