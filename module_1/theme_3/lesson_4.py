def practice_1():
    # Ввод количества чисел
    n = int(input("Введите количество чисел: "))

    # Ввод самих чисел
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    # Используем множество для хранения уникальных значений
    unique_numbers = set(numbers)

    # Вывод количества уникальных чисел
    print(len(unique_numbers))

def practice_2():
    # Ввод первого списка
    list1 = list(map(int, input("Введите числа первого списка: ").split()))

    # Ввод второго списка
    list2 = list(map(int, input("Введите числа второго списка: ").split()))

    # Переводим оба списка в множества
    set1 = set(list1)
    set2 = set(list2)

    # Находим пересечение и выводим его длину
    common = set1 & set2
    print(len(common))


def practice_3():
    # Ввод последовательности чисел
    numbers = list(map(int, input("Введите числа через пробел: ").split()))

    seen = set()

    for num in numbers:
        if num in seen:
            print("YES")
        else:
            print("NO")
            seen.add(num)


if __name__ == "__main__":
    practice_1()
    practice_2()
    practice_3()
