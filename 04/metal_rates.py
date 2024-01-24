# Вебинар #4
# регулярное вырадение для парсинга веб-страницы, полученной из сети
# Ведущий: Дмитрий Румянцев
# Python для аналитиков данных

from urllib.request import urlopen
import re

# страница со стоимостью дграгоценных металлов
url = 'https://cbr.ru/hd_base/metall/metall_base_upto/'

if __name__ == '__main__':

    try:
        # подключение к документу
        response = urlopen(url)
        # прочитать документ
        webdoc = response.read()
        # декодировать
        html = webdoc.decode()
    except OSError:
        print('Ошибка!')
    else:
        # регулярное выражение
        pattern = r'(\d{2}\.\d{2}\.\d{4})\D+' \
                  r'([\d\s]*\d{2,3},\d{4})\D+' \
                  r'([\d\s]*\d{2,3},\d{4})\D+' \
                  r'([\d\s]*\d{2,3},\d{4})\D+' \
                  r'([\d\s]*\d{2,3},\d{4})'

        # откомпилировать
        regex = re.compile(pattern)

        # получить данные
        golds = regex.findall(html)

        # вывести на консоль
        line = '-'*55
        print(line)
        print('   Дата    |  Золото  | Серебро |   Платина  | Палладий')
        print(line)
        # формирование таблицы
        for gold in reversed(golds):
            print('{} | {} | {} | {} | {}'.format(gold[0],gold[1],gold[2],gold[3],gold[4]))
        print(line)

