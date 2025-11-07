"""Скрипт запуска игры 'Наибольший общий делитель'."""

from VD_games.engine import run_game
from VD_games.games.gcd import generate_gcd_question


def run_gcd_game():
    """Запускает игру 'НОД'."""
    run_game(
        game_description='Find the greatest common divisor of given numbers.',
        generate_question_function=generate_gcd_question
    )


if __name__ == '__main__':
    run_gcd_game()
