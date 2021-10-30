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
    for item in a:
        if not c_1 < abs(item) > c_2:
            d.append(item)
    while len(d) != len(a):
        d.append(0)
    print(f"Новый массив: {d}")
