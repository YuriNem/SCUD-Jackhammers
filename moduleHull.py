# Нахождение множества точек, образующих оболочку, 
# содержащую все исходные точки
def getHull(points, lengthPoints):

    # Множество точек
    hull = []

    # Опрделение стороны нахождения точки относительно линии
    def findSide(pointLeft, pointRight, point):
        value = (point[1] - pointLeft[1]) * (pointRight[0] - pointLeft[0]) -\
         (pointRight[1] - pointLeft[1]) * (point[0] - pointLeft[0])
        if value > 0:
            return 1
        if value < 0:
            return -1
        return 0

    # Нахождние расстояния между линией и точкой
    def getDist(pointLeft, pointRight, point):
        return abs((point[1] - pointLeft[1]) * (pointRight[0] - pointLeft[0]) -\
         (pointRight[1] - pointLeft[1]) * (point[0] - pointLeft[0]))

    # pointLeft и pointRight образуют линию, 
    # делящую множество точек на 2 подмножества
    # side определяет подмножество, 1 - верхнее, -1 - нижнее
    def quickHull(points, lengthPoints, pointLeft, pointRight, side):
        # Нахождение индекса и длины максимально удаленной точки от линии 
        # по выбранную сторону от линии
        indexPointMaxDist = -1
        maxDist = 0
        for i in range(lengthPoints):
            dist = getDist(pointLeft, pointRight, points[i])
            if findSide(pointLeft, pointRight, points[i]) == side and dist > maxDist:
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
        quickHull(points, lengthPoints, points[indexPointMaxDist], pointLeft, -findSide(points[indexPointMaxDist], pointLeft, pointRight))
        quickHull(points, lengthPoints, points[indexPointMaxDist], pointRight, -findSide(points[indexPointMaxDist], pointRight, pointLeft))

    # Нахождение индексов карайней левой и правой точек
    indexMinX = 0
    indexMaxX = 0
    for i in range(1, lengthPoints):
        if points[i][0] < points[indexMinX][0]:
            indexMinX = i
        if points[i][0] > points[indexMaxX][0]:
            indexMaxX = i
    
    # Рекурсивное нахождение выпуклых точек оболочки сверху
    quickHull(points, lengthPoints, points[indexMinX], points[indexMaxX], 1)

    # Рекурсивное нахождение выпуклых точек оболочки снизу
    quickHull(points, lengthPoints, points[indexMinX], points[indexMaxX], -1)

    return hull
