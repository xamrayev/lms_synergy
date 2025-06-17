# Рекурсивная функция для вывода элементов списка
def recursive_print(my_list, index=0):
    if index < len(my_list):
        print(my_list[index])
        recursive_print(my_list, index + 1)
    else:
        print("Конец списка")

# Исходный список
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Вызов рекурсивной функции
recursive_print(my_list)
