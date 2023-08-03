import prompt


def run_game(game, n=3):
    # Greeting
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    print(game.DESCRIPTION)

    # Answering questions and checking answers
    for i in range(n):
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
            return
    else:
        print(f"Congratulations, {player_name}!")
