import prompt


def engine_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.CONDITION)

    round_counter = 1
    while round_counter <= 3:
        parameters = game.logic_game()
        print(f'Question: {parameters[0]}')
        question = prompt.string('Your answer: ')

        if str(parameters[1]) == question:
            print('Correct!')
            round_counter += 1
            if round_counter > 3:
                print(f'Congratulations, {name}!')
                break

        else:
            print(f"\'{question}\' is wrong answer ;(."
                  f" Correct answer was \'{parameters[1]}\'."
                  f"\nLet's try again, {name}!")
            break
