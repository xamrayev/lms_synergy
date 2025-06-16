def practice_1():
    # Ввод числа
    num = int(input("Введите целое число: "))

    # Проверка и описание числа
    if num == 0:
        print("нулевое число")
    elif num % 2 != 0:
        print("число не является четным")
    else:
        if num > 0:
            print("положительное четное число")
        else:
            print("отрицательное четное число")


def practice_2():
    # Ввод слова
    word = input("Введите слово из маленьких латинских букв: ")

    # Определяем гласные
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    vowel_counts = {v: 0 for v in vowels}

    # Подсчет
    for char in word:
        if char in vowels:
            vowel_count += 1
            vowel_counts[char] += 1
        else:
            consonant_count += 1

    # Проверка наличия всех гласных
    if all(vowel_counts[v] > 0 for v in vowels):
        print("Гласных букв:", vowel_count)
        print("Согласных букв:", consonant_count)
        print("Количество каждой гласной:", vowel_counts)
    else:
        print(False)


def practice_3():
    # Ввод данных
    X = int(input("Минимальная сумма инвестиций X: "))
    A = int(input("У Майкла есть A долларов: "))
    B = int(input("У Ивана есть B долларов: "))

    # Проверка условий
    if A >= X and B >= X:
        print(2)
    elif A >= X:
        print("Mike")
    elif B >= X:
        print("Ivan")
    elif A + B >= X:
        print(1)
    else:
        print(0)
