"""Универсальный движок для запуска игр."""

from VD_games.cli import welcome_user

def run_game(game_description, generate_question_function):
    """Запускает игру с общей логикой """
    name = welcome_user()
    print(game_description)
    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        question, correct_answer = generate_question_function()
        print(f'Question: {question}')

        user_answer = input('Your answer: ').strip()

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
