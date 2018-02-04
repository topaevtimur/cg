import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

from util.check import check
from util.create_SP import createSP
from util.draw_graph import drawGraph
from util.generate_points import generatePoints
from util.hull_go import hullGo
from util.intersect_line import intersect_line


def sweep_task(solution):

    polygon = generatePoints(20, 40, 0, 20, 7)
    hull = ConvexHull(polygon)
    polygon_np = np.array(polygon)

    point = [10, 10]

    fig, ax1 = createSP(plt);


    ax1.plot(point[0], point[1], 'ro');



    polygon_hul, ax1 = hullGo(hull, ax1, polygon_np, polygon)

    ans = solution(point, polygon_hul)

    print(ans)

    drawGraph(ans, ax1, fig)

    ans1 = naive_algorithm(point, polygon_hul)
    check(ans, ans1)

def naive_algorithm(point, polygon):

    points = list(polygon)
    points += point


    ans = []

    for p2 in polygon:
        t1 = list(point)
        t2 = list(p2)
        t2[0] -= 0.00001
        intersect = False

        for i in range(len(polygon) - 1):
            if intersect_line(t1, t2, polygon[i], polygon[i + 1]):
                intersect = True
        if intersect_line(t1, t2, polygon[-1], polygon[0]):
            intersect = True

        if not intersect:
            ans.append([t1, t2])

    return ans
