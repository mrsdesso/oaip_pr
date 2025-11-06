import random
from VD_games.cli import welcome_user

def is_even(number):
    """Возвращает 'yes', если число чётное, и 'no' - если нет."""
    return 'yes' if number % 2 == 0 else 'no'

def run_even_game():
    """Основная логика игры 'Проверка на чётность'."""
    # Приветствуем пользователя и получаем его имя
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_to_win = 3  # Количество правильных ответов подряд для победы
    correct_answers = 0

    # Игра продолжается, пока пользователь не даст 3 верных ответа подряд
    while correct_answers < rounds_to_win:
        # Генерируем случайное число
        question_number = random.randint(1, 100)
        print(f'Question: {question_number}')

        # Получаем ответ от пользователя
        user_answer = input('Your answer: ').strip().lower()

        # Вычисляем правильный ответ
        correct_answer = is_even(question_number)

        # Проверяем ответ пользователя
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            # Если ответ неверный, завершаем игру
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Выход из функции (завершение игры)

    # Если цикл завершился, значит, пользователь выиграл
    print(f'Congratulations, {name}!')

# Эта точка входа позволяет запускать игру напрямую: `python VD_even.py`
if __name__ == '__main__':
    run_even_game()
