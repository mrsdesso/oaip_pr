"""Логика игры 'Калькулятор'."""

import random


def calculate_expression(num1, num2, operator):
    """Вычисляет результат математического выражения."""
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError(f"Неизвестный оператор: {operator}")


def generate_calc_question():
    """Генерирует вопрос для игры 'Калькулятор'."""
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*'])

    correct_result = calculate_expression(number1, number2, operator)
    question = f"{number1} {operator} {number2}"

    return question, str(correct_result)
