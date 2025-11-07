import random
from VD_games.cli import welcome_user


def gcd(a, b):
    """Вычисляет наибольший общий делитель двух чисел."""
    while b:
        a, b = b, a % b
    return a


def generate_gcd_question():
    """Генерирует два числа и вычисляет их НОД."""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correct_answer = gcd(a, b)
    question = f"{a} {b}"
    return question, str(correct_answer)


def run_gcd_game():
    """Основная логика игры 'НОД'."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    rounds_to_win = 3
    correct_answers = 0

    while correct_answers < rounds_to_win:
        question, correct_answer = generate_gcd_question()
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


if __name__ == '__main__':
    run_gcd_game()
