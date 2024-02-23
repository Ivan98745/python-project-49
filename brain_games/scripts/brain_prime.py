#!/usr/bin/env python3

from brain_games import engine


def check_numb(numb):
    i = numb
    while i > 2:
        if numb % (i - 1) != 0:
            i -= 1
            result = 'yes'
        else:
            result = 'no'
            break
    return result


def logic_game():
    engine.greet()
    engine.welcome_user()
    rule_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    print(rule_game)
    count = 1
    while count <= 3:
        rand_num = engine.random_number(3, 100)
        print(f'Question: {rand_num}')
        result = check_numb(rand_num)
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
