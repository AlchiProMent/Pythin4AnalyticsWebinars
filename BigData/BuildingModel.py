# прогноз цен домов в Мельбурне

import pandas as pd
from environment import melbourne_file_path

# !pip install -U scikit-learn
from sklearn.tree import DecisionTreeRegressor

try:
    # прочитать данные
    print('Прочитать данные...')
    melbourne_data = pd.read_csv(melbourne_file_path)
except Exception as e:
    print(f'Ошибка чтения "{melbourne_file_path}"')
else:
    print('Данные успешно прочитаны.')

    # оставить только полные данные (удалить NA)
    melbourne_data = melbourne_data.dropna(axis=0)

    # dot-notation: получить столбец "Цены на жилье"
    y = melbourne_data.Price
    # выбор "фич" (Features)
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = melbourne_data[melbourne_features]

    # Определите модель. random_state задается явно, чтобы гарантировать одинаковые результаты при каждом запуске.
    melbourne_model = DecisionTreeRegressor(random_state=1)
    # обучить модель
    melbourne_model.fit(X, y)

    # сделать прогнозы
    print("Прогноз для первых пяти домов:")
    first_five = X.head()
    print(first_five)
    print("\nПрогноз цен:")
    print(melbourne_model.predict(first_five))




