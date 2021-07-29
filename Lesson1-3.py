"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

n = int(input("Введите число n: "))
number = str(n)
n2 = number + number
n3 = number + number + number
total = n + int(n2) + int(n3)
print("Сумма чисел n + nn + nnn равна:", total)

