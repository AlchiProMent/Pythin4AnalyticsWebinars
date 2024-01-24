# Вебинар #4
# Работа с файлами; конструкция try-except для защиты от аварийного завершения программы
# Ведущий: Дмитрий Румянцев
# Python для аналитиков данных

# импорт функции exists для проверки наличия файла на диске
from os.path import exists

file_name = 'metal_rates.py'
file_name2 = 'files.py'
file_name3 = 'new_file.txt'

if __name__ == '__main__':

    # программа открывает два файл, объединяет их содержимое вместе,
    # после чего выводит на консол и в новый файл (new_file.txt).

    try:
        # открыть и прочитать файл в кодировке utf-8
        with open(file_name, encoding='utf-8') as f:
            txt = f.read()
    except FileNotFoundError:
        # если обнаружена ошибка "нет файла"
        print(f'Файл {file_name} отсутствует!')
    else:

        # проверка наличия файла file_name2
        if exists(file_name2):
            with open(file_name2, encoding='utf-8') as f2:
                try:
                    txt2 = f2.read()
                except OSError as e:
                    # вывести стандартное соощение об ошибке через доступ к объекту, пописывающему ошибку
                    print(e.strerror)
                else:
                    # чтение второго файла прошло успешно

                    # объединить оба файла в одну переменную
                    txt3 = txt + '\n' + '-'*50 + '\n' + txt2
                    # вывести на консоль значение этой переменной (т.е. тект обоих файлов)
                    print(txt3)

                    try:
                        with open(file_name3, 'w', encoding='utf-8') as f3:
                            f3.write(txt3)
                    except OSError:
                        print(f'Ошибка при сохранении файла {file_name3}!')
                    else:
                        print(f'Файл {file_name3} успешно сохранен')

        else:
            print(f'Файл {file_name2} не найден!')

