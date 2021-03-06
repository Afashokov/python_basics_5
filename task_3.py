"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

# !!!!!!! Начало блока создания текста !!!!!!!
with open("task_3.txt", "w") as task3:
    task3.write('Иванов 23543.12\nПетров 13749.32\nСидоров 15191.46\nМельникова 39854.91\nКрылова 54268.12\n'
                'Кузнецов 19987.05\nКапустина 23814.82\nАнтонов 31593.14\nЧернова 19999.99\n'
                'Фомина 25834.67\nКудрявцева 257932.24')
# !!!!!!! Конец блока создания текста !!!!!!!
with open("task_3.txt", "r") as task3_text:
    content = [el.split() for el in task3_text.readlines()]
    print("Список сотрудников у которых оклад меньше 20 тыс.")
    summa_zarplat = 0
    for el in content:
        el[1] = float(el[1])
        if el[1] < 20000:
            print(f'{el[0]} с зарплатой {el[1]}')
        summa_zarplat += el[1]
    print(f'Средняя зарплата сотрудников равна {round(summa_zarplat / len(content), 2)}')
