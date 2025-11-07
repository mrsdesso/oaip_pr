"""Скрипт запуска игры 'Калькулятор'."""

from VD_games.engine import run_game
from VD_games.games.calc import generate_calc_question


def run_calc_game():
    """Запускает игру 'Калькулятор'."""
    run_game(
        game_description='What is the result of the expression?',
        generate_question_function=generate_calc_question
    )


if __name__ == '__main__':
    run_calc_game()
