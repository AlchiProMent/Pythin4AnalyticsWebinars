import pandas as pd
from environment import melbourne_file_path

try:
    # прочитать данные
    print('Прочитать данные...')
    melbourne_data = pd.read_csv(melbourne_file_path)
except Exception as e:
    print(f'Ошибка чтения "{melbourne_file_path}"')
else:
    # установить вывод всех столбцов
    pd.set_option('display.max_columns', None)

    print(f'Всего записей в таблице: {len(melbourne_data)}')
    # Генерация описательной статистики
    describe = melbourne_data.describe()

    print('\nСтатистика по столбцам:')
    # вывести данные
    print(describe)