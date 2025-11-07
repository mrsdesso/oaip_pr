"""Скрипт запуска игры 'Проверка на чётность'."""

from VD_games.engine import run_game
from VD_games.games.even import generate_even_question


def run_even_game():
    """Запускает игру 'Проверка на чётность'."""
    run_game(
        game_description='Answer "yes" if the number is even, otherwise answer "no".',
        generate_question_function=generate_even_question
    )


if __name__ == '__main__':
    run_even_game()
