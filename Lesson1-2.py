"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

user = input("Введите время в секундах: ")

user_time = int (user)
hours = user_time // 3600
minutes = (user_time // 60) % 60
seconds = user_time % 60

print(f"Время в формате чч:мм:сс: {hours}:{minutes}:{seconds}")
