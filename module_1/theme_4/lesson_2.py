import random

matrix_1 = [
    [0, -2, -1, -6, -6, 0, -9, -8, -30, -9],
    [5, 12, 4, -16, -4, -9, -16, -15, 1, -26],
    [13, 39, 14, 23, -4, 40, 32, 6, -8, 23],
    [13, -8, 34, 49, 30, 18, 47, 11, -24, 11],
    [21, 73, 71, 61, -1, 79, -34, 22, 69, 67],
    [75, 25, 25, 39, 100, -12, -21, 81, -10, 87],
    [81, 63, 102, 104, 53, -44, 71, -36, -36, -9],
    [7, 98, 26, -3, 128, 94, 18, -26, 14, 21],
    [65, 128, 80, 124, 27, -32, 73, 59, 19, 34],
    [43, 111, 38, 149, 5, 112, 79, 53, 15, 92]
]

matrix_2 = [
    [0, 4, 6, 11, 15, 6, 9, 26, 15, 21],
    [-5, 4, -15, -9, -4, 2, -8, 19, -4, -1],
    [-2, -39, -19, 14, 22, 5, -34, 15, 16, -9],
    [-22, -52, 11, -11, -3, 16, -11, -6, -32, -2],
    [-61, -47, -5, -58, 16, -13, 28, -36, -64, 2],
    [-29, 23, 19, 2, -14, -87, 7, -88, 39, 7],
    [-6, 18, -97, 26, -64, 0, -72, -34, -68, -92],
    [-120, -117, -72, -129, -139, 16, -61, 36, -137, -29],
    [-112, -83, 7, -119, -132, -129, -143, -154, -23, -34],
    [32, -67, -75, -92, 15, -163, 18, 31, -162, -16]
]

def add_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)

    return result


def generate_matrix(rows, cols, min_val=-150, max_val=150):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def practice_1():
    matrix_3 = add_matrices(matrix_1, matrix_2)

    print("Результат сложения matrix_1 и matrix_2:")
    for row in matrix_3:
        print(row)

def practice_2():
    # Генерируем случайные матрицы
    rows, cols = 10, 10
    m1 = generate_matrix(rows, cols)
    m2 = generate_matrix(rows, cols)

    # Складываем их
    m3 = add_matrices(m1, m2)

    print("\nМатрица 1:")
    for row in m1:
        print(row)

    print("\nМатрица 2:")
    for row in m2:
        print(row)

    print("\nСумма матриц:")
    for row in m3:
        print(row)
