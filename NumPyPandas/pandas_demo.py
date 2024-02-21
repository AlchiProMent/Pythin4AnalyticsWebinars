import pandas as pd

if __name__ == '__main__':
    print('Вектор')
    vect = pd.Series([12, 23, -5, 8])
    print(vect)
    print(vect.size)
    print(vect.shape)
    print(vect.ndim)
    print()

    print('Установка индексов')
    v2 = pd.Series([12, 23, -5, 8], index=['A B C D'.split()])
    print(v2)
    print(v2['B'])
    print()

    print('Объект DataFrame')
    mix_type_arr = [[11, 12, 'Смесь', False], [21, 22, 23, 24]]
    df = pd.DataFrame(mix_type_arr)
    print(df)
    print('\nИзменение индексов:')
    df.index = ['One', 'Two']
    print(df)

    print('\nИзменение столбцов:')
    df.columns = list('ABCD')
    print(df)
    print(df['C'])
    print('Транспонировать массив:')
    print(df.T)
    print()

    print('Книги на складе:')
    data = [['Хроники Нарнии', 'Льюис Клайв Стейплз', '978-5-04-194042-3', 2021, 2996.00, 120],
            ['Спасение дикого робота', 'Браун Питер', '978-5-00195-379-1', 2022, 1053.00, 24],
            ['Затерянный мир', 'Дойл Артур Конан', '978-5-17-122827-9', 2024, 182.00, 51],
            ['Звездный десант', 'Хайнлайн Роберт Энсон', '978-5-389-22217-5', 2022, 202.00, 18]]
    books = pd.DataFrame(data,
                         columns=['Title', 'Author', 'ISBN', 'Year', 'Price', 'Total'],
                         index=[ch for ch in 'ABCD'])

    pd.set_option('display.max_columns', None)
    print(books)
    print('\nВсего книг:', books['Total'].sum())
    print('Средняя цена:', books['Price'].mean())
    print()

    print("['Title', 'Price']")
    print(books[['Title', 'Price']])
    print()
    b = books[['Title', 'Price']]
    print(b[b['Price'] > 1000])
    print()

    print(books.loc['C', 'Title'])
    print()

    print(books.loc[['A', 'C'], ['Title', 'Price', 'Total']])
    print()

    print(books.iloc[0, 1])

    books.drop('B', inplace=True)
    print(books)
    print()

    books.drop('ISBN', axis=1, inplace=True)
    print(books)
    print()

