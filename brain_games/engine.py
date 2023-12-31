import prompt


ROUNDS_NUMBER = 3


def run_game(game):
    # Greeting
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(game.DESCRIPTION)

    # Answering questions and checking answers
    n = ROUNDS_NUMBER
    for _ in range(n):
        question, correct_answer = game.generate_game_data()
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
            n -= 1
        else:
            text = " is wrong answer ;(. Correct answer was "
            print(f"""'{answer}'{text}'{correct_answer}'.""")
            print(f"Let's try again, {player_name}!")
            break

    else:
        print(f"Congratulations, {player_name}!")
