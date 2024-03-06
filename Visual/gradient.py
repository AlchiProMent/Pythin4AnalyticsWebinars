# исследование градиентного спуска

import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(f_x,               # функция
                     gradient,          # градиент
                     start,             # стартовое значение
                     learn_rate,        # скорость обучения
                     n_iter=50,         # количество итераций
                     tolerance=1e-06,   # минимально допустимое перемещение на каждой итерации
                     ax_num=0):
    vector = start
    x = []
    y = []
    for ind, _ in enumerate(range(n_iter)):

        diff = -learn_rate * gradient(vector)
        x.append(vector)
        y.append(f_x(vector))

        # если обновление вектора мсеньше или равно tolerance, выйти из цикла итераций
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff

    ax[ax_num].plot(x, y, color='red')
    ax[ax_num].scatter(x, y, s=25, color='red')
    return vector


if __name__ == '__main__':
    x = np.linspace(-10, 10, 100)

    # исследуемая функция
    f_x = lambda v: v ** 2
    # градиент
    grad_x = lambda v: 2 * v

    y = f_x(x)

    fg, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 9))

    ax[0].plot(x, y)
    ax[0].set_title('Градиентный спуск')
    ax[0].grid()

    GD = gradient_descent(f_x=f_x, gradient=grad_x, start=10., learn_rate=.2)
    print('Минимум:', GD)

    x2 = np.linspace(-3, 3, 100)
    # исследуемая функция
    f_x2 = lambda v: v ** 4 - 5 * v ** 2 - 3 * v
    # градиент
    grad_x2 = lambda v: 4 * v ** 3 - 10 * v - 3
    y2 = f_x2(x2)
    ax[1].plot(x2, y2)
    ax[1].grid()

    GD = gradient_descent(f_x=f_x2, gradient=grad_x2, start=0, learn_rate=.1, ax_num=1)
    print()
    print('Минимум predict:', GD)

    plt.tight_layout()
    plt.show()
