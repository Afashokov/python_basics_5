# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# !!!!!!! Начало блока создания текста, необходим для всех примеров !!!!!!!
with open("task_6.txt", "w") as task6:
    task6.write('Информатика:   100(л)   50(пр)   20(лаб)\nФизика:   30(л)   —   10(лаб)\n'
                'Физкультура:   —   30(пр)   —\nЛитература:   150(л)   -   -\nХимия:   50(л)   30(пр)   80(лаб)')
# !!!!!!! Конец блока создания текста, необходим для всех примеров !!!!!!!
# !!!!!!! Начало блока пример 1 !!!!!!!
print('Пример без import re')
with open("task_6.txt") as task6_text:
    task6_dict = dict(el.split(':') for el in task6_text.readlines())
    for el in task6_dict.keys():
        temp_text = ''
        task6_dict[el] = task6_dict[el].replace("\n", ' ')
        for i in task6_dict.get(el):
            if i.isdecimal():
                temp_text += i
            else:
                temp_text += ' '
        temp_text = sum(int(number) for number in temp_text.split())
        task6_dict[el] = temp_text
    print(task6_dict)
# !!!!!!! Конец блока пример 1 !!!!!!!
# !!!!!!! Начало блока пример 2 !!!!!!!
print('Пример с import re (re.sub)')
import re

with open("task_6.txt") as task6_text:
    task6_dict = dict(el.split(':') for el in task6_text.readlines())
    for el in task6_dict.keys():
        task6_dict[el] = sum(int(i) for i in re.sub("[^0-9]", " ", task6_dict[el]).split())
    print(task6_dict)
# !!!!!!! Конец блока пример 2 !!!!!!!
