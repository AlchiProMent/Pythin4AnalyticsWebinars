# Операции линейной алгебры

import numpy as np

if __name__ == '__main__':
    m1 = np.array([[11, 12, 13],
                   [21, 22, 23]])

    m2 = np.array(
        [[2, 3],
         [4, 5],
         [6, 7]])

    m3 = np.arange(1, 7).reshape(2, 3)

    v1 = np.array([1, 2, 3]).reshape(3, 1)
    v2 = np.array([4, 5, 6]).reshape(3, 1)

    print('m1:')
    print(m1)
    print()

    print('m2:')
    print(m2)
    print()

    print('m3:')
    print(m3)
    print()

    print('v1:')
    print(v1)
    print()

    print('v1.reshape(3, ):')
    print(v1.reshape(3, ))
    print()

    print('v2:')
    print(v2)
    print()

    print('сложение матриц m1 + m3')
    print(m1 + m3)
    print()
    print('сложение m1 + v1.reshape(3, )')
    print(m1 + v1.reshape(3, ))
    print()

    print('скалярное умножения dot(m1, v1)')
    print(np.dot(m1, v1))
    print()
    print('скалярное умножения dot(m1, m2)')
    print(np.dot(m1, m2))
    print()
    print('скалярное умножения dot(m1, 3)')
    print(np.dot(m1, 3))
    print()
    print('скалярное умножения dot(v1.reshape(3, ), v2.reshape(3, ))')
    print(np.dot(v1.reshape(3, ), v2.reshape(3, )))
    print()

    # seed задается, чтобы при всех запусках программы рещультат был одинаковый
    rng = np.random.default_rng(seed=12345)
    a1 = rng.standard_normal(10)
    print('A1: Стандартное нормальное распределение:')
    print(a1)
    print()

    # фактически заменяет все отрицательные числа нулями
    print('A1: Поэлементные максимумы относительно нуля (RELU, Rectified linear unit):')
    for n in np.maximum(a1, 0):
        print(n, end='  ')
    print()
    print()

    # рзультат тот же, что у предыдущего блока, но за счёт прямой операции присваивания на основе булева индекса
    a1[a1 < 0] = 0
    print('A1: Все отрицательные числа заменены нулями (результат тот же):')
    for n in a1:
        print(n, end='  ')
    print()
    print()