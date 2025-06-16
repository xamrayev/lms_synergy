def practise_1():
    # Запрос информации о питомце
    vid = input("Введите вид питомца: ")
    vozrast = input("Введите возраст питомца: ")
    klichka = input("Введите кличку питомца: ")

    # Вывод результата
    print(f"Это {vid} по кличке \"{klichka}\". Возраст: {vozrast} лет.")

def practise_2():
    # Запрашиваем этапы развития человека
    stage1 = input("Введите первую стадию развития человека: ")
    stage2 = input("Введите вторую стадию: ")
    stage3 = input("Введите третью стадию: ")
    stage4 = input("Введите четвёртую стадию: ")
    stage5 = input("Введите пятую стадию: ")
    stage6 = input("Введите шестую стадию (например, Homo sapiens sapiens): ")

    # Выводим результат с разделителем =>
    print(stage1, stage2, stage3, stage4, stage5, stage6, sep=" => ")
