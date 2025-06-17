import collections

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not 12 <= age % 100 <= 14:
        return "года"
    else:
        return "лет"

def get_pet(ID):
    return pets[ID] if ID in pets else False

def pets_list():
    for ID in pets:
        pet_dict = pets[ID]
        for name, info in pet_dict.items():
            suffix = get_suffix(info["Возраст питомца"])
            print(f'{ID}. Это {info["Вид питомца"]} по кличке "{name}". Возраст: {info["Возраст питомца"]} {suffix}. Владелец: {info["Имя владельца"]}')

def create():
    if pets:
        last = collections.deque(pets, maxlen=1)[0]
        new_id = last + 1
    else:
        new_id = 1

    name = input("Имя питомца: ")
    species = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": species,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print("Питомец успешно добавлен!")

def read():
    ID = int(input("Введите ID питомца для отображения: "))
    pet_dict = get_pet(ID)
    if not pet_dict:
        print("Питомец с таким ID не найден.")
        return
    for name, info in pet_dict.items():
        suffix = get_suffix(info["Возраст питомца"])
        print(f'Это {info["Вид питомца"]} по кличке "{name}". Возраст: {info["Возраст питомца"]} {suffix}. Владелец: {info["Имя владельца"]}')

def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet_dict = get_pet(ID)
    if not pet_dict:
        print("Питомец с таким ID не найден.")
        return

    for name in pet_dict:
        print(f"Обновляем данные для '{name}'")
        new_species = input("Новый вид питомца: ")
        new_age = int(input("Новый возраст: "))
        new_owner = input("Новое имя владельца: ")
        pet_dict[name] = {
            "Вид питомца": new_species,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }
        print("Информация обновлена!")

def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    if ID in pets:
        del pets[ID]
        print("Питомец удалён.")
    else:
        print("Нет питомца с таким ID.")


def practice_1():
    # Ввод пользователя
    n = int(input("Введите натуральное число: "))

    # Вычисляем факториалы от n до 1
    factorial_list = [factorial(i) for i in range(n, 0, -1)]

    print("Список факториалов от", n, "до 1:", factorial_list)

def practice_2():
    while True:
        command = input("\nВведите команду (create/read/update/delete/list/stop): ").lower()
        if command == "stop":
            break
        elif command == "create":
            create()
        elif command == "read":
            read()
        elif command == "update":
            update()
        elif command == "delete":
            delete()
        elif command == "list":
            pets_list()
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

