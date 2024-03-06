from math import sin, cos

def prn(func_name, n):
    m = func_name(n)
    print('Значение фукнции:', m)

title = "Функция обратного вызова (callback) — это функция, которая передается другой функции в качестве аргумента"
str_len = len(title)
func_len = len
print(str_len)
str_len = func_len('Москва')
print(str_len)

f1 = lambda v: v**2

prn(f1, 3)

f2 = lambda v: sin(v)
f3 = lambda v: cos(v)

prn(f2, 1)
prn(f3, 1)
