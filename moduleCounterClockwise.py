import math

# Сортировка точек против часовой стрелки
def sortCounterClockwise(hull, lengthHull):

    # Замыкание центральной точки
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

    # Нахождение центральной точки
    centerPoint = getCenterPoint(hull, lengthHull)

    # Сортировка точек по углу против часовой стрелки
    sortedHull = sorted(hull, key=closureCenter(centerPoint))

    return sortedHull
