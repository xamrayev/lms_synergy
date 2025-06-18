import random
import time
import os
import json

class Game:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.helicopter_x = width // 2
        self.helicopter_y = height // 2
        self.helicopter_water = 0
        self.helicopter_max_water = 3
        self.helicopter_lives = 3
        self.score = 0
        self.tick = 0
        self.fires = []
        self.trees = []
        self.rivers = []
        self.hospital_x = 2
        self.hospital_y = 2
        self.shop_x = width - 3
        self.shop_y = 2
        self.clouds = []
        self.weather = "clear"  # clear, storm
        self.storm_duration = 0
        
        # Символы для отображения
        self.symbols = {
            'helicopter': '🚁',
            'tree': '🌲',
            'fire': '🔥',
            'river': '🌊',
            'burned': '💀',
            'hospital': '🏥',
            'shop': '🏪',
            'cloud': '☁️',
            'empty': '🟫'
        }
        
        self.init_game()
    
    def init_game(self):
        """Инициализация игрового поля"""
        # Очистка поля
        self.field = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Генерация рек
        self.generate_rivers()
        
        # Генерация деревьев
        self.generate_trees()
        
        # Размещение больницы и магазина
        self.field[self.hospital_y][self.hospital_x] = 'H'
        self.field[self.shop_y][self.shop_x] = 'S'
        
        print("Игра инициализирована!")
    
    def is_valid_cell(self, x, y):
        """Проверка, принадлежит ли клетка полю"""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def generate_rivers(self):
        """Генерация рек"""
        self.rivers = []
        
        # Горизонтальная река
        river_y = self.height // 3
        for x in range(self.width // 4, 3 * self.width // 4):
            if self.is_valid_cell(x, river_y):
                self.field[river_y][x] = 'R'
                self.rivers.append((x, river_y))
        
        # Вертикальная река
        river_x = self.width // 3
        for y in range(self.height // 4, 3 * self.height // 4):
            if self.is_valid_cell(river_x, y):
                self.field[y][river_x] = 'R'
                self.rivers.append((river_x, y))
    
    def generate_trees(self):
        """Генерация деревьев"""
        self.trees = []
        tree_count = (self.width * self.height) // 8
        
        for _ in range(tree_count):
            attempts = 0
            while attempts < 50:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                
                if (self.field[y][x] == ' ' and 
                    (x, y) != (self.helicopter_x, self.helicopter_y) and
                    (x, y) != (self.hospital_x, self.hospital_y) and
                    (x, y) != (self.shop_x, self.shop_y)):
                    
                    self.field[y][x] = 'T'
                    self.trees.append((x, y, 'healthy'))  # x, y, состояние
                    break
                attempts += 1
    
    def generate_random_cells(self):
        """Генерация случайных событий"""
        # Новые деревья
        if random.random() < 0.05:  # 5% шанс
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.field[y][x] == ' ':
                self.field[y][x] = 'T'
                self.trees.append((x, y, 'healthy'))
        
        # Облака
        if random.random() < 0.1:  # 10% шанс
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.clouds.append((x, y, 5))  # x, y, продолжительность
    
    def generate_fires(self):
        """Генерация пожаров"""
        if self.weather == "storm":
            fire_chance = 0.7  # Больше пожаров во время грозы
        else:
            fire_chance = 0.4  # Увеличили шанс пожара
        
        if random.random() < fire_chance and self.trees:
            # Выбираем случайное здоровое дерево
            healthy_trees = [(x, y) for x, y, state in self.trees if state == 'healthy']
            if healthy_trees:
                x, y = random.choice(healthy_trees)
                self.field[y][x] = 'F'
                self.fires.append((x, y, 5))  # x, y, время до распространения (увеличили время)
                
                # Обновляем состояние дерева
                for i, (tx, ty, state) in enumerate(self.trees):
                    if tx == x and ty == y:
                        self.trees[i] = (tx, ty, 'burning')
                        break
                
                print(f"🔥 ПОЖАР! Дерево загорелось в позиции ({x}, {y})!")
    
    def update_fires(self):
        """Обновление пожаров"""
        new_fires = []
        
        for x, y, time_left in self.fires:
            if time_left > 0:
                new_fires.append((x, y, time_left - 1))
            else:
                # Пожар распространяется
                self.field[y][x] = 'B'  # Сгоревшее дерево
                self.score -= 10
                
                # Удаляем дерево из списка
                self.trees = [(tx, ty, state) for tx, ty, state in self.trees 
                             if not (tx == x and ty == y)]
                
                # Распространение на соседние деревья
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if (self.is_valid_cell(nx, ny) and 
                            self.field[ny][nx] == 'T' and
                            random.random() < 0.4):
                            self.field[ny][nx] = 'F'
                            new_fires.append((nx, ny, 3))
                            
                            # Обновляем состояние дерева
                            for i, (tx, ty, state) in enumerate(self.trees):
                                if tx == nx and ty == ny:
                                    self.trees[i] = (tx, ty, 'burning')
                                    break
        
        self.fires = new_fires
    
    def update_weather(self):
        """Обновление погоды"""
        if self.weather == "storm":
            self.storm_duration -= 1
            if self.storm_duration <= 0:
                self.weather = "clear"
        else:
            if random.random() < 0.05:  # 5% шанс грозы
                self.weather = "storm"
                self.storm_duration = 10
    
    def update_clouds(self):
        """Обновление облаков"""
        self.clouds = [(x, y, duration - 1) for x, y, duration in self.clouds 
                       if duration > 1]
    
    def move_helicopter(self, dx, dy):
        """Перемещение вертолета"""
        new_x = self.helicopter_x + dx
        new_y = self.helicopter_y + dy
        
        if self.is_valid_cell(new_x, new_y):
            self.helicopter_x = new_x
            self.helicopter_y = new_y
            
            # Взаимодействие с клеткой
            cell = self.field[new_y][new_x]
            
            if cell == 'R':  # Река - набираем воду
                self.helicopter_water = min(self.helicopter_water + 1, 
                                          self.helicopter_max_water)
                print(f"Набрали воду! Воды: {self.helicopter_water}")
            
            elif cell == 'F':  # Пожар - тушим
                if self.helicopter_water > 0:
                    self.helicopter_water -= 1
                    self.field[new_y][new_x] = 'T'
                    self.score += 20
                    
                    # Удаляем пожар
                    self.fires = [(x, y, t) for x, y, t in self.fires 
                                 if not (x == new_x and y == new_y)]
                    
                    # Обновляем состояние дерева
                    for i, (tx, ty, state) in enumerate(self.trees):
                        if tx == new_x and ty == new_y:
                            self.trees[i] = (tx, ty, 'healthy')
                            break
                    
                    print(f"Потушили пожар! Очки: {self.score}")
                else:
                    print("Нет воды для тушения!")
            
            elif cell == 'H':  # Больница
                if self.score >= 50:
                    self.helicopter_lives += 1
                    self.score -= 50
                    print(f"Восстановили здоровье! Жизни: {self.helicopter_lives}")
                else:
                    print("Недостаточно очков для лечения!")
            
            elif cell == 'S':  # Магазин
                if self.score >= 100:
                    self.helicopter_max_water += 1
                    self.score -= 100
                    print(f"Увеличили резервуар! Максимум воды: {self.helicopter_max_water}")
                else:
                    print("Недостаточно очков для улучшения!")
    
    def display_field(self):
        """Отображение игрового поля"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"🚁 Очки: {self.score} | ❤️ Жизни: {self.helicopter_lives} | 💧 Вода: {self.helicopter_water}/{self.helicopter_max_water}")
        print(f"🌤️ Погода: {self.weather} | ⏰ Ход: {self.tick}")
        print(f"🔥 Активных пожаров: {len(self.fires)} | 🌲 Деревьев: {len([t for t in self.trees if t[2] == 'healthy'])}")
        print("-" * (self.width * 2 + 1))
        
        for y in range(self.height):
            row = "|"
            for x in range(self.width):
                if x == self.helicopter_x and y == self.helicopter_y:
                    row += self.symbols['helicopter']
                elif (x, y) in [(cx, cy) for cx, cy, _ in self.clouds]:
                    row += self.symbols['cloud']
                elif self.field[y][x] == 'T':
                    row += self.symbols['tree']
                elif self.field[y][x] == 'F':
                    row += self.symbols['fire']
                elif self.field[y][x] == 'R':
                    row += self.symbols['river']
                elif self.field[y][x] == 'B':
                    row += self.symbols['burned']
                elif self.field[y][x] == 'H':
                    row += self.symbols['hospital']
                elif self.field[y][x] == 'S':
                    row += self.symbols['shop']
                else:
                    row += self.symbols['empty']
                row += " "
            row += "|"
            print(row)
        
        print("-" * (self.width * 2 + 1))
        print("🎮 Управление: W-вверх, S-вниз, A-влево, D-вправо, Q-выход, P-пауза")
        print("💾 1-сохранить, 2-загрузить | 🏥-больница(50💰), 🏪-магазин(100💰)")
    
    def save_game(self, filename="savegame.json"):
        """Сохранение игры"""
        game_data = {
            'width': self.width,
            'height': self.height,
            'field': self.field,
            'helicopter_x': self.helicopter_x,
            'helicopter_y': self.helicopter_y,
            'helicopter_water': self.helicopter_water,
            'helicopter_max_water': self.helicopter_max_water,
            'helicopter_lives': self.helicopter_lives,
            'score': self.score,
            'tick': self.tick,
            'fires': self.fires,
            'trees': self.trees,
            'rivers': self.rivers,
            'weather': self.weather,
            'storm_duration': self.storm_duration
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(game_data, f)
            print("Игра сохранена!")
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
    
    def load_game(self, filename="savegame.json"):
        """Загрузка игры"""
        try:
            with open(filename, 'r') as f:
                game_data = json.load(f)
            
            self.width = game_data['width']
            self.height = game_data['height']
            self.field = game_data['field']
            self.helicopter_x = game_data['helicopter_x']
            self.helicopter_y = game_data['helicopter_y']
            self.helicopter_water = game_data['helicopter_water']
            self.helicopter_max_water = game_data['helicopter_max_water']
            self.helicopter_lives = game_data['helicopter_lives']
            self.score = game_data['score']
            self.tick = game_data['tick']
            self.fires = game_data['fires']
            self.trees = game_data['trees']
            self.rivers = game_data['rivers']
            self.weather = game_data['weather']
            self.storm_duration = game_data['storm_duration']
            
            print("Игра загружена!")
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
    
    def game_over(self):
        """Проверка окончания игры"""
        return self.helicopter_lives <= 0
    
    def run(self):
        """Основной игровой цикл"""
        print("Добро пожаловать в игру 'Вертолет-пожарный'!")
        print("Ваша задача - тушить пожары и спасать лес!")
        print("Управление: W-вверх, S-вниз, A-влево, D-вправо, Q-выход")
        print("1-сохранить, 2-загрузить, P-пауза")
        input("Нажмите Enter для начала игры...")
        
        while not self.game_over():
            self.display_field()
            
            # Простое получение ввода
            print("Введите команду (w/a/s/d/q/p/1/2): ", end="")
            try:
                key = input().lower().strip()
                
                if key == 'w':
                    self.move_helicopter(0, -1)
                elif key == 's':
                    self.move_helicopter(0, 1)
                elif key == 'a':
                    self.move_helicopter(-1, 0)
                elif key == 'd':
                    self.move_helicopter(1, 0)
                elif key == 'q':
                    print("Выход из игры...")
                    break
                elif key == 'p':
                    input("Игра на паузе. Нажмите Enter для продолжения...")
                elif key == '1':
                    self.save_game()
                elif key == '2':
                    self.load_game()
                elif key == '':
                    # Пустой ввод - пропускаем ход
                    pass
                else:
                    print("Неизвестная команда!")
                
                # Обновление игрового состояния каждый ход
                self.generate_fires()  # Генерируем пожары каждый ход
                
                if self.tick % 2 == 0:  # Каждые 2 хода
                    self.generate_random_cells()
                
                self.update_fires()
                self.update_weather()
                self.update_clouds()
                
                # Урон от грозы
                if (self.weather == "storm" and 
                    (self.helicopter_x, self.helicopter_y) in [(x, y) for x, y, _ in self.clouds]):
                    if random.random() < 0.3:
                        self.helicopter_lives -= 1
                        print("Вертолет поврежден грозой!")
                        time.sleep(1)
                
                self.tick += 1
                
            except KeyboardInterrupt:
                print("\nВыход из игры...")
                break
            except Exception as e:
                print(f"Ошибка: {e}")
                continue
        
        print(f"Игра окончена! Финальный счет: {self.score}")

def game():
    """Главная функция"""
    print("Игра 'Вертолет-пожарный'")
    
    # Выбор размера поля
    try:
        width = int(input("Введите ширину поля (по умолчанию 20): ") or 20)
        height = int(input("Введите высоту поля (по умолчанию 15): ") or 15)
    except ValueError:
        width, height = 20, 15
    
    game = Game(width, height)
    game.run()

if __name__ == "__main__":
    game()