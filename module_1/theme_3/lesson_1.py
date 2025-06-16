def practice_1():
    # Ввод количества чисел
    N = int(input("Введите количество чисел: "))

    count_zero = 0
    print(f"Введите {N} целых чисел:")

    # Вводим N чисел и считаем нули
    for _ in range(N):
        num = int(input())
        if num == 0:
            count_zero += 1

    print("Количество нулей:", count_zero)


def practice_2():
    import math

    # Ввод числа
    X = int(input("Введите натуральное число X (≤ 2*10^9): "))

    count = 0
    limit = int(math.isqrt(X)) + 1

    # Перебираем делители от 1 до √X
    for i in range(1, limit):
        if X % i == 0:
            count += 1  # i — делитель
            if i != X // i:
                count += 1  # X // i — тоже делитель, если не равен i

    print("Количество натуральных делителей:", count)

def practice_3():
    # Вводим A и B
    A = int(input("Введите A (начало диапазона): "))
    B = int(input("Введите B (конец диапазона, A ≤ B): "))

    # Список чётных чисел
    even_numbers = [str(i) for i in range(A, B + 1) if i % 2 == 0]

    # Вывод через пробел
    print("Четные числа на отрезке:")
    print(' '.join(even_numbers))
