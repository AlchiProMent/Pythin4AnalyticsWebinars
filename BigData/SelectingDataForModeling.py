
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
    # вывести данные
    print('Столбцы:')
    print(melbourne_data.columns)
    print()

    # удалить пропущенные значения
    melbourne_data = melbourne_data.dropna(axis=0)

    # получить столбец "Цены на жилье"
    y = melbourne_data.Price
    print('Цены на жилье:')
    print(y[:10])
    print()

    # выбор "фич" (Количество комнат, количество спален, размер земли, широта, долгота)
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = melbourne_data[melbourne_features]
    print('Первые пять домовладений:')
    print(X[:5])
    print()
    print(X.describe())
