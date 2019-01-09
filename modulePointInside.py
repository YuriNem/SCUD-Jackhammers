# Проверка расположения точки внутри
def isPointInside(point, sortedHull, lengthHull):
    # Координаты проверяемой точки
    x, y = point

    # Флаг
    isInside = False

    # Координаты 2 соседних точек
    point1X, point1Y = hull[0]
    for i in range(1, lengthHull + 1):
        point2X, point2Y = hull[i % lengthHull] 

        # Проверяем координату y
        if y > min(point1Y, point2Y):
            if y <= max(point1Y, point2Y):
                # Проверяем координату x справо
                if x <= max(point1X, point2X):
                    # Если у точек разные координаты по y, 
                    # то находим максимально возможный x для проверяемой точки по y
                    if point1Y != point2Y:
                        maxX = (y - point1Y) * (point2X - point1X) / (point2Y - point1Y) + point1X
                    
                    # Если координаты по x точек равны 
                    # или x проверяемой точки меньше максимально возможного x,
                    # то точка лежит внутри
                    if point1X == point2X or x <= maxX:
                        isInside = not isInside

        # Проверяем следующие 2 соседние точки
        point1X, point1Y = point2X, point2Y
    
    return isInside
