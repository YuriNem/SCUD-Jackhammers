#!/usr/bin/env python3

import sys

# Модуль для нахождения оболочки
import moduleHull

# Модуль для сортировки точек против часовой стрелки
import moduleCounterClockwise

# Модуль для нахождения площади
import moduleSquare

# Модуль для проверки расположения точки внутри
import modulePointInside

# Открытие входного файла на чтение
fileInput = open(sys.argv[1], 'r')

# Список границ стран
bordersCountries = []

# Площадь отключения
squareOutage = 0

# Колличество построек
amountBuildings = int(fileInput.readline())

while amountBuildings != -1:
    # Чтение координат x и y построек и создание списка 
    # из точек с такими координатами
    points = []
    for i in range(amountBuildings):
        x, y = map(int, fileInput.readline().split())
        point = [x, y]
        points.append(point)
    
    # Нахождение оболочки
    hull = moduleHull.getHull(points, len(points))

    # Сортировка точек оболочки против часовой стрелки
    sortedHull = \
     moduleCounterClockwise.sortCounterClockwise(hull, len(hull))

    # Добавление отсортированной оболочки в список границ стран
    bordersCountries.append(sortedHull)

    amountBuildings = int(fileInput.readline())

# Строка координат рокет
rocketCoordinatesLine = fileInput.readline()

while rocketCoordinatesLine:
    # Чтение координат x и y рокеты и создание точки
    # с такими координатами
    x, y = map(int, rocketCoordinatesLine.split())
    point = [x, y]

    # Проверка всех стран на расположение точки внутри них
    for i in range(len(bordersCountries)):
        if modulePointInside.isPointInside(point, \
            bordersCountries[i], len(bordersCountries[i])):
            # Если точка расположена в стране,
            # то находиться ее площадь и прибавляется к площади отключения
            square = moduleSquare.getSquare(bordersCountries[i], len(bordersCountries[i]))
            squareOutage += square
            break
        
    rocketCoordinatesLine = fileInput.readline()

# Закрытие входного файла
fileInput.close()

# Открытие, запись полощади отключения 
# и закрытие выходного файла
fileOutput = open(sys.argv[2], 'w')
fileOutput.write('{:.2f}'.format(squareOutage))
fileOutput.close()
