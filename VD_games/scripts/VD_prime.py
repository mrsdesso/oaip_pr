"""Скрипт запуска игры 'Простое ли число?'."""

from VD_games.engine import run_game
from VD_games.games.prime import generate_prime_question

def run_prime_game():
    """Запускает игру 'Простое ли число?'."""
    run_game(
        game_description='Answer "yes" if given number is prime. Otherwise answer "no".',
        generate_question_function=generate_prime_question
    )

if __name__ == '__main__':
    run_prime_game()
