# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open("task_1.txt", "w+") as task_1:
    while True:
        user_input = input("Введите строку или нажмите Enter без ввода, для завершения программы >>> ")
        if len(user_input) == 0:
            print("Завершение ввода")
            break
        else:
            print(user_input, file=task_1)
            # task_1.write(f'{user_input}\n')
# task_1 = open("task_1.txt")
# print(task_1.read())
# task_1.close()
