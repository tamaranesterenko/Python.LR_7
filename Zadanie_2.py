#/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = list(map(float, input("Введите элементы массива: ").split()))
    d = list()
    c_1 = float(input("Введите начало интервала для удаления: "))
    c_2 = float(input("Введите конец интервала для удаления: "))

    a.sort()
    print(f"Отсортированный массив: {a}")
    print(f"Максимальное число: {max(a)}")
    b = list(filter(lambda x: x<0, a))
    print(f"Сумма отрициательных элементов: {sum(b)}")
    d = list(filter(lambda x: c_1 < x < c_2, a))
    print('d = {}\n'.format(d))
    while len(a) != len(d):
        d.extend('0')
    print(f"Новый массив: {d}")
