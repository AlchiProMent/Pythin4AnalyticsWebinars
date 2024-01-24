# Вебинар #3
# Классы и библиотеки
# Ведущий: Дмитрий Румянцев
# Python для аналитиков данных

# импортирование из библиотеки math функций вычисления факториала и находдления синуса
from math import factorial, sin

# иллюстрация создания простого класса MathClass
class MathClass:
    def __init__(self, n):
        self._n = n

    def squ(self):
        return self._n*self._n

    def prn(self):
        print(self.squ())

if __name__ == '__main__':

    print(__name__)
    n = 23
    # факториал числа
    f = factorial(n)
    print(f)
    print(f'Синус {n}:', sin(n))
    print()

    # создание экземпляра класса MathClass
    match = MathClass(10)
    # получить значение куба числа
    print(match.squ())
