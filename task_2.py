"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

# !!!!!!! Начало блока создания текста, необходим для всех примеров !!!!!!!
with open("task_2.txt", "w") as task2:
    task2.write('если прибавить три к пяти получится восемь\n'
                'или 3 + 5 = 8\n'
                'являются ли числа и спецсимволы словами я не знаю - скорее всего нет\n'
                'хотя если прочитать их прочитать их  7 семь  , запятая  - минус или тире    чем не слова\n'
                '  может считаться словом лишь в двух случаях - когда прямо так написан или произнесен    пробел\n'
                'во всех остальных случаях это всего лишь пустота - отсутствие символов или слов\n'
                'this is a sample text it should not mean anything')
# !!!!!!! Конец блока создания текста, необходим для всех примеров !!!!!!!
# !!!!!!! Начало блока пример 1!!!!!!!
print(r"Пример 1, спецсимволы и числа считаются словами, при этом \n и пробел - не считаются")
with open("task_2.txt") as task2_text:
    content = task2_text.readlines()
    for i in range(len(content)):
        print(f"{i + 1}-я строка, {len(content[i].split())} слов")
# !!!!!!! Конец блока пример 1!!!!!!!
# !!!!!!! Начало блока пример 2!!!!!!!
print(r"Пример 2, спецсимволы не считаются словами")
with open("task_2.txt", "r") as task2_text:
    content = task2_text.readlines()
    for i in range(len(content)):
        counter, position = 0, 'outer'
        for el in content[i]:
            if el.isalnum() and position == 'outer':
                counter += 1
                position = 'inner'
            elif el == ' ':
                position = 'outer'
        print(f"{i + 1}-я строка, {counter} слов")
# !!!!!!! Конец блока пример 2!!!!!!!
# !!!!!!! Начало блока пример 3!!!!!!!
print(r"Пример 3, спецсимволы и числа не считаются словами")
with open("task_2.txt", "r") as task2_text:
    content = task2_text.readlines()
    for i in range(len(content)):
        counter, position = 0, 'outer'
        for el in content[i]:
            if el.isalpha() and position == 'outer':
                counter += 1
                position = 'inner'
            elif el == ' ':
                position = 'outer'
        print(f"{i + 1}-я строка, {counter} слов")
# !!!!!!! Конец блока пример 3!!!!!!!
