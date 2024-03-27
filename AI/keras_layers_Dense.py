# Реализация слоя keras.layers.Dense

import numpy as np
import time

def naive_relu(x):
    # реализация keras-функции relu (rectified linear unit)
    if len(x.shape) == 2:

        x = x.copy()
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                x[i, j] = max(x[i, j], 0)

        # с помощью NumPy этот алгорит 'relu' реализуется одной строкой: z = np.maximum[z, 0.]

        return x
    else:
        return None


def naive_add(x:np.ndarray, y:np.ndarray):
    # "ручная" реализация умножения массивов
    if (len(x.shape) == 2) and (x.shape == y.shape):
        x = x.copy()
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                x[i, j] += y[i, j]

        # с помощью NumPy этот алгорит реализуется одной строкой: z = x + y
        return x
    else:
        return None

def naive_add_matrix_and_vector(x, y):
    if (len(x.shape) == 2) and (len(y.shape) == 1) and (x.shape[1] == y.shape[1]):

        x = x.copy()
        for i in range(x.shape[0]):
            for j in range(x.shape[1]):
                x [i, j] += y[j]
        return x
    else:
        return None

def naive_vector_dot(x, y):
    # склаярное произведение двух векторов
    if (len(x.shape) == 1) and (len(y.shape) == 1) and (x.shape[0] == y.shape[0]):
        z = 0.
        for i in range(x.shape[0]):
            z += x[i] * y[y]
        return z
    else:
        return None

def naive_matrix_vector_dot(x, y):
    # скалярное произведение матрицы на вектор
    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        z[i] = naive_vector_dot(x[i,:], y)
    return z

def naive_matrix_dot(x, y):
    # склаярное произведение матриц
    # количество столбцов x должно равняться количеству строку y
    if (len(x.shape) == 2) and (len(y.shape) == 2) and (x.shape[1] == y.shape[0]):
        # создать нулевоую матрицу заданной формы
        z = np.zeros((x.shape[0], y.shape[1]))
        for i in range(x.shape[0]):
            for j in range(y.shape[1]):
                row_x = x[i, :]
                column_y = y[:, j]
                z[i, j] = naive_vector_dot(row_x, column_y)
        return z
    else:
        return None

if __name__ == '__main__':

    # реализации формулы:
    # output = relu(dot(input, W) + b)

    # проверить скорость работы алгоритмов созданных "ручных" функций и функций NumPy

    x = np.random.random((20, 100))
    y = np.random.random((20, 100))

    print('Использование средств NumPy')
    t0 = time.time()
    for _ in range(1000):
        z = x + y
        z = np.maximum(z, 0)
    t1 = time.time()
    print(f'Всего {t1 - t0:.2f} сек.')
    t0 = time.time()
    for _ in range(1000):
        z = x + y
        z[z < 0] = 0
    t1 = time.time()
    print(f'Всего {t1 - t0:.6f} сек.')

    print()
    print('"Ручные" функции')
    t0 = time.time()
    for _ in range(1000):
        z2 = naive_add(x, y)
        z2 = naive_relu(z2)
    t1 = time.time()
    print(f'Всего {t1 - t0:.2f} сек.')
