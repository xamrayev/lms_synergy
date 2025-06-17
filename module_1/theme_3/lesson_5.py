def practice_1():
    pets = {}

    # Запрашиваем количество питомцев
    n = int(input("Сколько питомцев вы хотите добавить? "))

    for i in range(n):
        print(f"\nПитомец №{i+1}")
        name = input("Введите имя питомца: ")
        species = input("Введите вид питомца: ")
        age = int(input("Введите возраст питомца: "))
        owner = input("Введите имя владельца: ")

        # Добавляем в словарь
        pets[name] = {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }

    print("\nИнформация о питомцах:")
    for pet_name, pet_info in pets.items():
        age = pet_info["Возраст питомца"]

        # Склонение слова "год"
        if age % 10 == 1 and age % 100 != 11:
            age_str = f"{age} год"
        elif 2 <= age % 10 <= 4 and not 12 <= age % 100 <= 14:
            age_str = f"{age} года"
        else:
            age_str = f"{age} лет"

        print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {age_str}. Имя владельца: {pet_info["Имя владельца"]}.')


def practice_2():
    my_dict = {}

    for i in range(10, -6, -1):  # от 10 до -5 включительно
        try:
            my_dict[i] = i ** i
        except:
            my_dict[i] = "Ошибка (нельзя возвести отрицательное в отрицательную степень)"

    print("\nСловарь степеней:")
    for k, v in my_dict.items():
        print(f"{k}: {v}")

