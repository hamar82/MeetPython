
"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой
 """


def main(**kwargs):
     return f"{kwargs['first_name']} {kwargs['last_name']} ({kwargs['year']}), {kwargs['city']}, {kwargs['phone']}, {kwargs['email']}"


user_name = input("Имя: ")
user_last_name = input("Фамилия: ")
user_year = int(input("Год рождения: "))
user_city = input("Город: ")
user_email = input("email: ")
user_phone = input("Номер телефона: ")

print(
    main(first_name=user_name, last_name=user_last_name,
         year=user_year, city=user_city, email=user_email,
         phone=user_phone)
)




