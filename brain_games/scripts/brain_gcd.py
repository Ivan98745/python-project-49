#!/usr/bin/env python3


from brain_games import engine


def logic_game():
    engine.greet()
    engine.welcome_user()
    rule_game = 'Find the greatest common divisor of given numbers.'
    print(rule_game)
    count = 1
    while count <= 3:
        rand_num_1 = engine.random_number(1, 100)
        rand_num_2 = engine.random_number(1, 100)
        print(f'Question: {rand_num_1} {rand_num_2}')
        while rand_num_1 != rand_num_2:
            if rand_num_1 > rand_num_2:
                rand_num_1 = rand_num_1 - rand_num_2
            else:
                rand_num_2 = rand_num_2 - rand_num_1
        result = rand_num_2
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
