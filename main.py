#!/usr/bin/env python3

import sys

# Модуль для нахождения оболочки
import moduleHull

# Модуль для нахождения площади
import moduleSquare

# Открытие переданного файла на чтение
file = open(sys.argv[1], 'r')

# Список стран
countries = []

while True:
    # Чтение колличества построек
    amountBuildings = int(file.readline())

    if amountBuildings == -1:
        break
    
    # Чтение координат x и y построек и создание списка из них
    points = []
    for i in range(amountBuildings):
        x, y = map(int, file.readline().split())
        point = [x, y]
        points.append(point)
    
    # Нахождение оболочки
    hull = moduleHull.getHull(points, len(points))

    # Нахождение площади
    square = moduleSquare.getSquare(hull, len(hull))

    # Создание словаря страны и добавление его в список стран
    country = {
        'hull': hull,
        'square': square,
    }
    countries.append(country)

print(countries)
