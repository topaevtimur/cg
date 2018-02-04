def area(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def intersect1(x1, y1, x2, y2):
    if x1 > y1:
        x1, y1 = y1, x1
    if x2 > y2:
        x2, y2 = y2, x2
    return max(x1, x2) <= min(y1, y2)


def intersect_line(a, b, c, d):
    return (intersect1(a[0], b[0], c[0], d[0])
            and intersect1(a[1], b[1], c[1], d[1])
            and area(a, b, c) * area(a, b, d) <= 0
            and area(c, d, a) * area(c, d, b) <= 0)

