
from IPython.display import display
from random import randint


def check(ans, ans1):
    ans.sort()
    ans1.sort()

    if ans1 == ans:
        print("Accepted")
    else:
        print("WA 1")


def createSP(plt):
    fig = plt.figure(figsize=(6, 6))
    ax1 = plt.subplot(111, aspect='equal')
    ax1.set_xlim(-5,45)
    ax1.set_ylim(-5,25)
    return fig, ax1



def drawGraph(ans, ax1, fig) :
    for v in ans:
        p1 = v[0]
        p2 = v[1]
        ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color='r', linestyle='-', linewidth=1)

    display(fig)

def generatePoints(x1, x2, y1, y2, N):
    points = {(randint(x1, x2), randint(y1, y2)) for i in range(N)}
    while len(points) < N:
        points |= {(randint(x1, x2), randint(y1, y2))}
    return list(list(x) for x in points)

def hullGo (hull, ax, poly_np, poly) :
    tmp_poly_hul = []
    for simplex in hull.simplices:
        ax.plot(poly_np[simplex, 0], poly_np[simplex, 1], 'k-')
    for v in hull.vertices:
        tmp_poly_hul.append(poly[v])
    return tmp_poly_hul, ax

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

