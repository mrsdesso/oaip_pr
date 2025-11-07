'''Игра арифметическая прогрессия '''
import random

def generate_arithmetic_progression():
    # Генерируем начальный элемент и шаг прогрессии
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    # Длина прогрессии от 5 до 10 элементов
    length = random.randint(5, 10)

    # Создаем прогрессию
    progression = [start + i * step for i in range(length)]

    # Выбираем случайную позицию для скрытого элемента
    hidden_index = random.randint(0, length - 1)

    # Сохраняем правильный ответ
    correct_answer = progression[hidden_index]

    # Создаем строку вопроса с двумя точками вместо скрытого элемента
    progression_display = progression.copy()
    progression_display[hidden_index] = '..'
    question = ' '.join(map(str, progression_display))

    return question, str(correct_answer)
