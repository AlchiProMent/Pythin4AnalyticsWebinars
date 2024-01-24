# Вебинар #2
# Ведущий: Дмитрий Румянцев
# Python для аналитиков данных


def run(x=2, y=3, *params):
    print('Данные:', x, y)
    # распаковка переданных параметров
    for p in params:
        print(p)

def demo(**wargs):
    # распаковка именованных параметров

    # распаковка в цикле
    for key, val in wargs.items():
        print(f'{key}={val}')

    # получение значения через явное указание имени парметра (при неверно указанном имени возникнет ошибка)
    print(wargs['sum'])
    print(wargs['total'])

if __name__ == '__main__':

    # передача функции упакованных параметров
    x = 321
    run(15, 123, 'Дополнительные параметры:', 23, 25, 5.2, 222, x)
    print()

    # передача именнованных параметров
    demo(s='Сумма', sum=120.5, total=200, count=5)
    print()

    # работа с конструкций if
    for n in range(1, 61):
        if (n % 3) == 0:
            print(f'{n} делится на 3 без остатка')
        elif (n % 7) == 0:
            print(f'{n} делится на 7 без остатка')
        else:
            print(n)

    # цикл
    for i in range(4):
        print(i)

    print()
    for n in range(1, 61):
        # выбор нескольких альтернатив
        match n:
            case 12:
                print('Это дюжина')
            case 16:
                print('Это пуд')
            case _:
                print(n)

    print()
    # простая и "мокрая" (RAW) строка
    print('12\t23\n34\t55')
    print(r'12\t23\n34\t55')