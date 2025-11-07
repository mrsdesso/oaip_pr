import random
from VD_games.cli import welcome_user


def calculate_expression(num1, num2, operator):
    # Используем match (как рекомендовано в задании)
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            # На случай, если передали неизвестный оператор
            raise ValueError(f"Неизвестный оператор: {operator}")


def generate_math_question():
    # Генерируем случайные числа от 1 до 20 (чтобы не слишком сложно)
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)

    # Выбираем случайный оператор
    operator = random.choice(['+', '-', '*'])

    # Вычисляем правильный ответ
    correct_result = calculate_expression(number1, number2, operator)

    # Формируем вопрос для пользователя
    question = f"{number1} {operator} {number2}"

    # Возвращаем вопрос и правильный ответ (в виде строки)
    return question, str(correct_result)


def run_calc_game():
    # Приветствуем пользователя и получаем имя
    user_name = welcome_user()

    # Объясняем правила игры
    print('What is the result of the expression?')

    # Настройки игры
    rounds_to_win = 3  # Нужно 3 правильных ответа подряд
    current_correct_answers = 0

    # Главный игровой цикл
    while current_correct_answers < rounds_to_win:
        # Генерируем новый вопрос
        question_text, correct_answer = generate_math_question()

        # Показываем вопрос пользователю
        print(f'Question: {question_text}')

        # Получаем ответ от пользователя
        user_answer = input('Your answer: ').strip()

        # Проверяем ответ
        if user_answer == correct_answer:
            print('Correct!')
            current_correct_answers += 1
        else:
            # Если ответ неверный - завершаем игру
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return  # Выходим из функции (игра завершена)

    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    run_calc_game()
