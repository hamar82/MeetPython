"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_string: str):
        numbers = Date.extract(date_string)
        self.validate(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def extract(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "Неверный формат числа"
        assert 1 <= m <= 12, "Неверный формат месяца"
        assert 1970 <= y <= 2100, "Неверный формат года"


my_date = Date('24-08-2021')




