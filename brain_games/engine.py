import prompt


def starts_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.CONDITION)

    rounds_count = 3
    for i in range(rounds_count):
        expression, result = game.get_question_nad_answer()
        print(f'Question: {expression}')
        question = prompt.string('Your answer: ')

        if str(result) != question:
            print(f"'{question}' is wrong answer ;(."
                  f" Correct answer was '{result}'."
                  f"\nLet's try again, {name}!")
            return

        print('Correct!')
    print(f'Congratulations, {name}!')
