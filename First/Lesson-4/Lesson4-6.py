"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
 не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

"""

from itertools import count

for el in count(int(input("Введите число: "))):
    if el > 10:
        break
    print(el)

from itertools import cycle

cycling_list = [10, 20, 30, 40, 50]
max_iterations = 30
iteration_count = 0

for el in cycle(cycling_list):
    print(el)
    iteration_count += 1

    if iteration_count >= max_iterations:
        break


