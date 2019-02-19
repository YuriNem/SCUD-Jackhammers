# Проверка расположения точки внутри
def isPointInside(point, sortedHull, lengthHull):
    # Состояние нахождения точки
    isInside = False

    # Координаты проверяемой точки
    x, y = point

    # Координаты 1 соседней точки
    point1X, point1Y = sortedHull[0]
    for i in range(1, lengthHull + 1):
        # Координаты 2 соседней точки
        point2X, point2Y = sortedHull[i] if i < lengthHull else sortedHull[0]

        # Ограничение по y (снизу, сверху)
        minY, maxY = min(point1Y, point2Y), max(point1Y, point2Y)

        # Ограничение по x (справо)
        maxX = max(point1X, point2X)

        # Проверяем вхождение точки в ограничения
        if minY < y <= maxY and x <= maxX:
            # Если координаты по x соседних точек равны, то точка лежит внутри
            if point1X == point2X:
                isInside = not isInside
            else:
                # Находим максимально возможный x для проверяемой точки по y
                maxXInside = (y - point1Y) * (point2X - point1X) /\
                 (point2Y - point1Y) + point1X
                    
                # Если x проверяемой точки меньше максимально возможного x 
                # для данного y, то точка лежит внутри
                if x < maxXInside:
                    isInside = not isInside

        # Проверяем следующие 2 соседние точки
        point1X, point1Y = point2X, point2Y
    
    return isInside
