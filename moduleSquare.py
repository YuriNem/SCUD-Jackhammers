import math

# Нахождение площади
def getSquare(hull, lengthHull):
    
    # Замыкание центральной точку
    def closureCenter(centerPoint):
        # Нахождение угола против часовой стрелки
        def getCounterClockwiseAngle(point):
            return math.degrees(math.atan2(point[1] - centerPoint[1],\
             point[0] - centerPoint[0]))
        
        return getCounterClockwiseAngle

    # Нахождение центральной точки
    def getCenterPoint(hull, lengthHull):
        # Сумма координат по x и y
        sumX = 0
        sumY = 0
        for i in range(lengthHull):
            sumX += hull[i][0]
            sumY += hull[i][1]
        
        # Координаты центра по x и y
        centerX = round(sumX / lengthHull, 2)
        centerY = round(sumY / lengthHull, 2)

        return [centerX, centerY]

    centerPoint = getCenterPoint(hull, lengthHull)

    # Сортировка по углу против часовой стрелки
    sortedHull = sorted(hull, key=closureCenter(centerPoint))

    # Формула площади Гаусса
    square = sortedHull[lengthHull - 1][0] * sortedHull[0][1] -\
     sortedHull[0][0] * sortedHull[lengthHull - 1][1]
    for i in range(lengthHull - 1):
        square += sortedHull[i][0] * sortedHull[i + 1][1] -\
         sortedHull[i + 1][0] * sortedHull[i][1]
    square = 1/2 * square

    return square
