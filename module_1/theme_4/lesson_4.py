# Родительский класс
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Класс-наследник
class Autobus(Transport):
    pass

def practice_1():
    # Создание объекта
    bus = Autobus("Renault Logan", 180, 12)

    # Вывод
    print(f"Название автомобиля: {bus.name}")
    print(f"Скорость: {bus.max_speed}")
    print(f"Пробег: {bus.mileage}")


# Родительский класс
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Наследуемый класс с переопределением метода
class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

def practice_2():
    # Создание автобуса
    bus = Autobus("Renault Logan", 180, 12)

    # Вывод вместимости
    print(bus.seating_capacity())


if __name__ == "__main__":
    practice_1()
    practice_2()