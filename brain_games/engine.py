import prompt


def starts_the_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.CONDITION)

    roundsCount = 3
    for i in range(roundsCount):
        parameters = game.describes_the_logic()
        print(f'Question: {parameters[0]}')
        question = prompt.string('Your answer: ')

        if str(parameters[1]) == question:
            print('Correct!')
            if i == roundsCount - 1:
                print(f'Congratulations, {name}!')

        else:
            print(f"\'{question}\' is wrong answer ;(."
                  f" Correct answer was \'{parameters[1]}\'."
                  f"\nLet's try again, {name}!")
            break
