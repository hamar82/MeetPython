"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""

def summary():
    try:
        with open('file_5.txt', 'w+') as input_data:
            line = input('Введите цифры через пробел:  \n')
            input_data.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()


