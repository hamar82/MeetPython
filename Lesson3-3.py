
"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
 """

def my_func(arg1, arg2, arg3):
    items = [arg1, arg2, arg3]
    items.remove(min(items))

    return sum(items)

a, b, c = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: "))

print(my_func(a, b, c))



