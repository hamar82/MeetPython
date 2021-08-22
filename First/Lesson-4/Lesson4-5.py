"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
 числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

numbers = [item for item in range(100, 1000 + 1) if item % 2 == 0]

multiplication = reduce(lambda x, y: x * y, numbers, 1)

print(multiplication)

