# Нахождение площади
def getSquare(sortedHull, lengthHull):

    # Формула площади Гаусса
    square = sortedHull[lengthHull - 1][0] * sortedHull[0][1] -\
     sortedHull[0][0] * sortedHull[lengthHull - 1][1]
    for i in range(lengthHull - 1):
        square += sortedHull[i][0] * sortedHull[i + 1][1] -\
         sortedHull[i + 1][0] * sortedHull[i][1]
    square = 1/2 * square

    return square
