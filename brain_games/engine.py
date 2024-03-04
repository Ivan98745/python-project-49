import prompt


def engine_game(game):
    greeting = 'Welcome to the Brain Games!'
    print(f'{greeting}')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    part_1 = 'is wrong answer ;(. Correct answer was'
    part_2 = "\nLet's try again, "
    condition = game.logic_game()
    print(condition[2])
    count = 1
    while count <= 3:
        parameters = game.logic_game()
        print(f'Question: {parameters[0]}')
        question = prompt.string('Your answer: ')
        if str(parameters[1]) == question:
            print('Correct!')
            count += 1
            if count > 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f"\'{question}\' {part_1} \'{parameters[1]}\'."
                  f"{part_2}{name}!")
            break
