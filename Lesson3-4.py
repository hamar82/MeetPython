
"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
 """

def my_func(x, y):

    return x ** y
 
"""
def exe_41(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x
   """

for i in range(abs(y - 1)):
    x *= x
return 1 / x


a, b = float(input("Введите первое число: ")), int(input("Введите второе число: "))

print(my_func(a, b))
"""


def power(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))

