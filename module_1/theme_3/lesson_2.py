def practice_1():
    # Ввод количества чисел
    N = int(input("Введите количество чисел: "))

    # Ввод N чисел в отдельной строке каждое
    numbers = [int(input()) for _ in range(N)]

    # Переворот массива
    reversed_numbers = numbers[::-1]

    # Вывод в одну строку
    print("Перевернутый массив:")
    print(*reversed_numbers)
    # Ввод количества чисел

def practice_2():
    # Ввод N и чисел
    N = int(input("Введите количество элементов: "))
    arr = list(map(int, input("Введите числа через пробел: ").split()))

    # Проверка на соответствие длины
    if len(arr) != N:
        print("Ошибка: введено неверное количество чисел.")
    else:
        # Перестановка по условию
        modified = []
        for i in range(N):
            if i == 0:
                modified.append(arr[-1])
            else:
                modified.append(arr[i - 1])
        
        # Вывод
        print("Изменённый массив:")
        print(*modified)

def practice_3():
    # Вводим максимальную массу лодки
    m = int(input("Введите максимальную массу лодки: "))

    # Вводим количество рыбаков
    n = int(input("Введите количество рыбаков: "))

    # Вводим веса рыбаков
    weights = [int(input()) for _ in range(n)]

    # Сортировка по весу
    weights.sort()

    # Два указателя: лёгкий и тяжёлый
    i = 0
    j = n - 1
    boats = 0

    while i <= j:
        # Если самые лёгкий и тяжёлый помещаются вместе — садим в одну лодку
        if weights[i] + weights[j] <= m:
            i += 1
        # Тяжёлого сажаем одного
        j -= 1
        boats += 1

    print("Минимальное количество лодок:", boats)
