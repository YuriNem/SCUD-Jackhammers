#!/usr/bin/env python3

import sys

# Модуль для нахождения оболочки
import moduleHull

# Модуль для сортировки точек против часовой стрелки
import moduleSortCounterClockwise

# Модуль для нахлждения площади
import moduleSquare

# Модуль для проверки расположения точки внутри
import moduleIsPointInside

# Открытие входного файла на чтение
fileInput = open(sys.argv[1], 'r')

# Список границ стран
bordersCountries = []

# Площадь отключения
squareOutage = 0

while True:
    # Чтение колличества построек
    amountBuildings = int(fileInput.readline())

    # Начало чтения координат рокет
    if amountBuildings == -1:
        while True:
            # Проверка конца файла
            line = fileInput.readline()
            if line == '':
                break

            # Чтение координат x и y рокеты и создание точки
            # с такими координатами
            x, y = map(int, line.split())
            point = [x, y]

            # Проверка всех стран на расположение точки внутри них
            for i in range(len(bordersCountries)):
                if moduleIsPointInside.isPointInside(point,\
                 bordersCountries[i], len(bordersCountries[i])):
                    # Если точка расположена в стране,
                    # то находиться ее площадь и прибавляется к площади отключения
                    square = moduleSquare.getSquare(bordersCountries[i], len(bordersCountries[i]))
                    squareOutage += square
                    break
        
        # Прекращение чтения файла
        break

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
    sortedHull =\
     moduleSortCounterClockwise.sortCounterClockwise(hull, len(hull))

    # Добавление отсортированной оболочки в список границ стран
    bordersCountries.append(sortedHull)

# Закрытие входного файла
fileInput.close()

# Открытие, запись полощади отключения 
# и закрытие выходного файла
fileOutput = open(sys.argv[2], 'w')
fileOutput.write('{:.2f}'.format(squareOutage))
fileOutput.close()
