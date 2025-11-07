"""Логика игры 'Простое ли число?."""

import random


def is_prime(number):
    """ Проверяет, является ли число простым. True если число простое, False если составное"""
    if number < 2:
        return False
    # Проверяем делители от 2 до квадратного корня из числа
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def generate_prime_question():
    # Генерируем случайное число от 1 до 50
    number = random.randint(1, 50)

    # Определяем правильный ответ
    correct_answer = 'yes' if is_prime(number) else 'no'

    return str(number), correct_answer
