"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""




with open("file_3.txt") as f:
    worker_list = [worker_line.split() for worker_line in f.readlines()]

workers_info = [
    {"name": worker[0], "salary": float(worker[1])}
    for worker in worker_list
    if len(worker) > 1
]

for worker in workers_info:
    if worker['salary'] < 20000:
        print("Сотрудник с окладом менее 20 тыс.: ", worker['name'])


