"""Скрипт запуска игры Арифметическая прогрессия"""

from VD_games.engine import run_game
from VD_games.games.progression import generate_arithmetic_progression


def run_progression_game():
    """Запускает игру 'Арифметическая прогрессия'."""
    run_game(
        game_description='What number is missing in the progression?',
        generate_question_function=generate_arithmetic_progression
    )


if __name__ == '__main__':
    run_progression_game()
