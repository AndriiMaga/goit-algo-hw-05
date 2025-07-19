import re # імпортуємо модуль для роботи з регулярними виразами

def generator_numbers(text: str): # генератор чисел з тексту
    value_1 = r"\s\d+\.\d+\s" # Регулярний вираз для пошуку дійсних чисел відокремлених пробілами з обох боків
    matches = re.findall(value_1, text) # Знаходимо всі дійсні числа з крапкою (float)
    for match in matches:
        yield float(match) # перетворюємо рядок на float

def sum_profit(text: str, func):
    numbers = func(text) # отримуємо генератор чисел з тексту
    total = 0 # зиінна для зберігання суми
    for number in numbers: # ітеруємось по числах, длдаючи кожне число до загальної суми
        total += number
    return total

text = "An employee's total income consists of three parts: 1200.5 is basic income and 25.45 and 375.00 are supplements"
result = sum_profit(text, generator_numbers)
print(f"Total income: {result}")
