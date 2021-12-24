# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# !!!!!!! Начало блока создания текста, необходим для всех примеров !!!!!!!
with open("task_4.txt", "w") as task4:
    task4.write('One — 1\nTwo — 2\nThree — 3\nFour — 4')
# !!!!!!! Конец блока создания текста, необходим для всех примеров !!!!!!!
# !!!!!!! Начало блока пример 1 !!!!!!!
result1 = 'ru1'
print(f'1-й способ task_4_{result1}.txt ' * 2)
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("task_4.txt") as task4_text:
    content = task4_text.readlines()
    for i in range(len(content)):
        content[i] = content[i].split()
        content[i][0] = my_dict.get(content[i][0])
    for i in range(len(content)):
        temp_txt = ''
        for el in content[i]:
            temp_txt += ''.join(f'{el} ' if el != content[i][len(content[i]) - 1] else f'{el}')
        content[i] = temp_txt
        if i < len(content) - 1:
            content[i] = f'{content[i]}\n'
    task4_result = open(f"task_4_{result1}.txt", 'w')
    for el in content:
        task4_result.write(el)
    task4_result.close()
# !!!!!!! Конец блока пример 1 !!!!!!!
# !!!!!!! Начало блока пример 2 !!!!!!!
result2 = 'ru2'
print(f'2-й способ task_4_{result2}.txt ' * 2)
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("task_4.txt") as task4_text:
    content = task4_text.readlines()
    for el in translate.keys():
        for i in range(len(content)):
            if el in content[i]:
                content[i] = content[i].replace(el, translate.get(el))
    task4_result = open(f"task_4_{result2}.txt", 'w')
    for el in content:
        task4_result.write(el)
    task4_result.close()
# !!!!!!! Конец блока пример 2 !!!!!!!
# !!!!!!! Начало блока пример 3 !!!!!!!
result = 'easiest_method'
translater = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
print(f'самый простой способ task_4_{result}.txt')
with open("task_4.txt") as task4_text, open(f'task_4{result}.txt', "w") as task4_easiest:
    easiest_method = task4_text.read()
    for el in translate.keys():
        easiest_method = easiest_method.replace(el, translater.get(el))
    task4_easiest.write(easiest_method)
    # print(easiest_method)
# !!!!!!! Конец блока пример 3 !!!!!!!
