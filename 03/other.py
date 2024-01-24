# Вебинар #3
# Работа со строками, последовательности, lambda-функции
# Ведущий: Дмитрий Румянцев
# Python для аналитиков данных

# экспорт класса MathClass из модуля about_lib
from about_lib import MathClass

def div4(n):
    return n % 4 == 0

def ft(x, y):
    return x*y, x, y

if __name__ == '__main__':

    mc = MathClass(5)
    mc.prn()

    s = 'Москва - столица России'
    print(s.replace('-', ':'))
    print(s.find('ск'))
    sa = s.split('-')
    print(sa)

    s2 = '12,23,34,44,12,44,55'
    nums = s2.split(',')

    l = [1, 2, 3, 4, 5, 6]
    print(l)
    l[3] = 55
    print(l)
    print(l[2:5])
    l2 = l.copy()
    print('l2:', l2)
    l2[1] = 123
    print('l2:', l2)
    print('l:', l)

    l3 = [n for n in range(1, 26)]
    print(l3)

    print(list(filter(div4, l3)))

    fn = lambda a: a % 5 == 0
    print(list(filter(fn, l3)))

    sq = lambda n: n**2
    print(list(map(sq, l3)))

    print(nums)
    s2n = lambda s: int(s)
    na = list(map(s2n, nums))
    print(na)

    '''
    sa = input('Ведите числа: ')
    try:
        na = list(map(s2n, sa.split()))
    except ValueError:
        print('Ошибка данных!')
    except:
        print('Неизвестная ошибка!')
    else:
        print(na)
    '''

    print()
    x = [1, 2, 3, 4, 5]
    y = [2]*5
    print(x)
    print(y)

    # упаковка массив функций zip
    for a, b in zip(x, y):
        print(f'{a} x {b} = {a*b}')

    # использование enumerate для получения номера очередной итерации цикла
    for i, a in enumerate(x):
        print(a * y[i])

    a = (1, 2, 3, 4)
    a2 = 12, 23, 34
    print(a2)

    z, *_ = ft(45, 55)
    print(z, _)

    d = {'name':'Paul', 'age': 23}
    d['summa'] = 10_000
    d['sex'] = 'm'
    print(d['age'])
    d[23] = 23000
    print(d)

    print('name' in d)
    for key, val in d.items():
        print(key, val, sep=': ')

    s = {2, 3, 4, 5, 6}
    print(s)

    a23 = [23.2, 3, 'Строку', True]
    print(a23)

    d12 = {1: 101,
           2: 23,
           3: 321,
           4: 12}

    # сортировка справочника
    sorted_d = dict(sorted(d12.items(), key=lambda item: item[1], reverse=True))
    print()
    for key, var in sorted_d.items():
        print(key, var)

