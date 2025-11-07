"""Логика игры 'Проверка на чётность'."""

import random


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0


def generate_even_question():
    """Генерирует вопрос для игры 'Чётность'."""
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer
