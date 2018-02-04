from random import randint



def generatePoints(x1, x2, y1, y2, N):
    points = {(randint(x1, x2), randint(y1, y2)) for i in range(N)}
    while len(points) < N:
        points |= {(randint(x1, x2), randint(y1, y2))}
    return list(list(x) for x in points)