# примеры работы с массивами ndarray

import numpy as np
from numpy import random as rnd

if __name__ == '__main__':

    arr = np.arange(1000)
    print(f'Размер массива: {arr.size:,}')

    print('Попытка создания массива смешанных значений')
    mix_type_arr = np.array([[11, 12, True, False], [21, 22, 23, 24]])
    print(mix_type_arr)
    print()

    print('Вектор')
    lst = [1, 2, 3, 4]
    print(lst)
    print(type(lst))
    a1D = np.array([1, 2, 3, 4])
    print(a1D)
    print(type(a1D))
    print(f'{a1D.ndim}-D')
    print('Размерность:', a1D.shape)
    print('Элементов:', a1D.size)
    print()

    print('Матрица')
    a2D = np.array([[11_1, 12_2, 13_5], [21_3, 22_4, 23_6]])
    print(a2D)
    print(f'{a2D.ndim}-D')
    print('Размерность:', a2D.shape)
    print('Строк:', a2D.shape[0])
    print('Столбцы:', a2D.shape[1])
    print('Элементов:', a2D.size)

    print()

    print('3-мерный массив (3D)')
    a3D = np.array([[[1_11_1, 1_12_2], [1_21_3, 1_22_4]], [[2_11_5, 2_12_6], [2_21_7, 2_22_8]]])
    print(a3D)
    print(f'{a3D.ndim}-D')
    print('Размерность:', a3D.shape)
    print('Элементов:', a3D.size)
    print()

    print('Создание массива при помощи генератора')
    arr = np.array([x for x in range(-10, 10 + 1) if x % 3 == 0 and x > 0])
    print(arr)
    print()

    print('Установка типа при создании массива')
    a = np.array([127, 128, 129])
    a2 = np.array([127, 128, 129], dtype=np.float32)
    print(a)
    print(a2)
    print()

    print('Генерация массивов стандартными методами NumPy')
    a3 = np.arange(10)
    a4 = np.arange(2, 10, dtype=float)
    a5 = np.arange(2, 3.1, 0.1)
    print(a3)
    print(a4)
    print(a5)
    print()

    print('Создание массива с равномерно распределенными между start и stop значениями')
    a6 = np.linspace(1.,5., 6)
    print(a6)
    print()

    print('Работа со случайными числами')
    ran_n = rnd.rand()
    a7 = rnd.random(6)
    a8 = rnd.randint(1, 100, 5)
    a9 = rnd.uniform(1, 100, 5)
    a10 = rnd.randn(3, 5)

    print('Случайное числое от 0 до 1:', ran_n)
    print(a7)
    print(a8)
    print(a9)
    print()
    print(a10)
    print()

    print('Создание массивов с указанием диагоналей')
    qmatrx = np.eye(3)
    print(qmatrx)
    print()

    qm4x7 = np.eye(4, 7)
    print(qm4x7)
    print()

    dmtrx = np.diag([11, 22, 33, 44, 55])
    print(dmtrx)
    print()

    print(np.diag(a2D))
    print()

    print('Массивы с нулевыми и единичными значениями')
    zero_arr = np.zeros((3, 5))
    print(zero_arr)
    print()
    ones_arr = np.ones((3, 5))
    print(ones_arr)
    print()

    print('Объединение массивов')
    sub_arr1 = np.ones((3, 3))
    sub_arr2 = np.eye(3, 3)
    sub_arr3 = np.zeros((3, 3))
    sub_arr4 = np.diag((44, 55, 66))
    matrix = np.block([[sub_arr1, sub_arr2], [sub_arr3, sub_arr4]])
    print(matrix)
    print()

    print('Срезы')
    slice = matrix[:, 3]
    print(slice.reshape(slice.size, 1))
    slice2 = matrix[[3,5], 2:5]
    print(slice2)



