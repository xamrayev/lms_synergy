class Kassa:
    def __init__(self):
        self.balance = 0

    def top_up(self, x):
        self.balance += x

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, x):
        if x > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= x

def practice_1():
    k = Kassa()
    k.top_up(2500)
    print("Тысяч в кассе:", k.count_1000())  # → 2
    k.take_away(1500)
    print("Осталось:", k.balance)  # → 1000

class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Скорость не может быть ≤ 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)
        if dx % self.s != 0 or dy % self.s != 0:
            return -1  # нельзя дойти ровно за шаги длиной s
        return dx // self.s + dy // self.s


def practice_2():
    t = Turtle(0, 0, 2)
    t.go_up()
    t.go_right()
    print(t.x, t.y)  # → 2 2
    print("Ходов до (4, 6):", t.count_moves(4, 6))  # → 4
    t.evolve()
    print("Новая скорость:", t.s)  # → 3

if __name__ == "__main__":
    practice_1()
    practice_2()