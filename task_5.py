# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
with open("task_5.txt", "w") as task5_text:
    try:
        number_min = int(input('Укажите минимальное значение числа >>> '))
        number_max = int(input('Укажите максимальное значение числа >>> '))
        numbers_in_string = int(input('Укажите количество чисел на строку >>> '))
        if number_min >= number_max:
            print('Неверный ввод. Максимальное число должно быть больше минимального')
            exit()
        for i in range(int(input('Напишите количество случайных чисел которые хотите записать в файл >>> '))):
            temp_number = str(random.randint(number_min, number_max))
            temp_number += '\n' if (i + 1) % numbers_in_string == 0 else temp_number + ' '
            # if (i + 1) % numbers_in_string == 0:
            #     temp_number += '\n'
            # else:
            #     temp_number += ' '
            task5_text.write(temp_number)
    except ValueError:
        print('Некорректный ввод. Требуется целое число')
        exit()
with open("task_5.txt") as task5_text:
    print(f'Сумма чисел = {sum(int(el) for el in task5_text.read().split())}')
