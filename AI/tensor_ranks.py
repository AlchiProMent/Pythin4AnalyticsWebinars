# Ранги тензоров

import numpy as np

if __name__ == '__main__':
    print('Скаляры. Тензоры 0-го ранга.')
    x = np.array(12)
    print(x)
    print('Осей:', x.ndim)
    print('Форма:', x.shape)
    print()

    print('Векторы. Тензоры 1-го ранга.')
    x = np.array([12, 3, 6, 14, 7])
    print(x)
    print('Осей:', x.ndim)
    print('Форма:', x.shape)
    print()

    print('Матрицы. Тензоры 2-го ранга.')
    x = np.array([[5, 78, 2, 34, 0],
                  [6, 79, 3, 35, 1],
                  [7, 80, 4, 36, 2]])
    print(x)
    print('Осей:', x.ndim)
    print('Форма:', x.shape)
    print()

    print('Тензоры 3-го ранга.')
    x = np.array([[[7, 12, 45, 6],
                   [12, 34, 22, 8],
                   [5, 12, 78, 11]],
                  [[23, 1, 5, 4],
                   [34, 0, 5, 87],
                   [5, 3, 67, 42]]])
    print(x)
    print('Осей:', x.ndim)
    print('Форма:', x.shape)
