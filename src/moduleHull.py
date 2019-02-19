# Нахождение множества точек, образующих оболочку, 
# содержащую все исходные точки
def getHull(points, lengthPoints):

    def getValue(pointLeft, pointRight, point):
        return (point[1] - pointLeft[1]) * (pointRight[0] - pointLeft[0]) -\
         (pointRight[1] - pointLeft[1]) * (point[0] - pointLeft[0])

    # Нахождние расстояния между линией и точкой
    def getDist(pointLeft, pointRight, point):
        return abs(getValue(pointLeft, pointRight, point))

    # Опрделение стороны нахождения точки относительно линии
    def findSide(pointLeft, pointRight, point):
        distSide = getValue(pointLeft, pointRight, point)
        if distSide > 0:
            return 1
        elif distSide < 0:
            return -1
        else:
            return 0

    # pointLeft и pointRight образуют линию, 
    # делящую множество точек на 2 подмножества
    # side определяет подмножество, 1 - верхнее, -1 - нижнее
    def createHull(hull, points, lengthPoints, pointLeft, pointRight, side):
        # Нахождение индекса и длины максимально удаленной точки от линии 
        # по выбранную сторону от линии
        indexPointMaxDist = -1
        maxDist = 0
        for i in range(lengthPoints):
            pointSide = findSide(pointLeft, pointRight, points[i])
            dist = getDist(pointLeft, pointRight, points[i])
            if pointSide == side and dist > maxDist:
                indexPointMaxDist = i
                maxDist = dist

        # Если точки не найдены, то точки, образующие линию, 
        # являются крайними
        if indexPointMaxDist == -1:
            if hull.count(pointLeft) == 0:
                hull.append(pointLeft)
            if hull.count(pointRight) == 0:
                hull.append(pointRight)
            return
        
        # Рекурсивное нахождение выпуклых точек оболочки для двух частей, 
        # разделенных максимально удаленной точкой
        createHull(hull, points, lengthPoints, points[indexPointMaxDist], pointLeft, \
         -findSide(points[indexPointMaxDist], pointLeft, pointRight))
        createHull(hull, points, lengthPoints, points[indexPointMaxDist], pointRight, \
         -findSide(points[indexPointMaxDist], pointRight, pointLeft))

    # Множество точек
    hull = []

    # Нахождение индексов карайней левой и правой точек
    indexMinX = 0
    indexMaxX = 0
    for i in range(1, lengthPoints):
        if points[i][0] > points[indexMaxX][0]:
            indexMaxX = i
        elif points[i][0] < points[indexMinX][0]:
            indexMinX = i
    
    # Рекурсивное нахождение выпуклых точек оболочки сверху
    createHull(hull, points, lengthPoints, points[indexMinX], points[indexMaxX], 1)

    # Рекурсивное нахождение выпуклых точек оболочки снизу
    createHull(hull, points, lengthPoints, points[indexMinX], points[indexMaxX], -1)

    return hull
