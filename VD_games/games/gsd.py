"""Логика игры НОД"""

import random


def find_gcd(a, b):
    """Находит наибольший общий делитель двух чисел."""
    while b != 0:
        a, b = b, a % b
    return a


def generate_gcd_question():
    """Генерирует вопрос для игры 'НОД'."""
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    correct_gcd = find_gcd(number1, number2)
    question = f"{number1} {number2}"

    return question, str(correct_gcd)
