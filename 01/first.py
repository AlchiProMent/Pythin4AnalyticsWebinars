# Вебинар #1
# Ведущий: Дмитрий Румянцев
# Python для аналитиков данных

# создание переменных
k = 123
a = b = c = d = e = f = 678
print(a, b, c, d, e, f, k)
print('b = ', b)
s = 'Это простая строка'
print(s)

x, y = 5, 10
print(x, y)

def a(x):
    # простая функция квадрата числа x
    return x**2

# влияние регистра символов на идентификатор переменных
key_of_string = 12
print(key_of_string)
Key_of_string = 12
print(Key_of_string)

n = 120
m = 3
print(n / m)
print(n // m)
print(n % m)
print(a(5))

# конкатенация строковых значений
s1 = 'Язык'
s2 = "Python"
s3 = "don't"
s4 = s1 + ' ' + s2 + ' ' + s3
print(s4)

print(45*12)
line = '-'
print(line*50)

# логические переменные и операции
t = True
f = False

print(12 > 5)
print(12 > 15)
