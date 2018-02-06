import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

from utils import*

def naive_task(solution):


    first_poly = generatePoints(0, 20, 0, 20, 7)
    second_poly = generatePoints(20, 40, 0, 20, 7)
    hull1 = ConvexHull(first_poly)
    hull2 = ConvexHull(second_poly)
    first_poly_np = np.array(first_poly)
    second_poly_np = np.array(second_poly)

    fig, ax1 = createSP(plt)

    first_poly_hul, ax1 = hullGo(hull1, ax1, first_poly_np, first_poly)
    second_poly_hul, ax1 = hullGo(hull2, ax1, second_poly_np, second_poly)



    ans = solution(first_poly_hul, second_poly_hul)

    drawGraph(ans, ax1, fig)

    ans1 = naive_algorithm(first_poly_hul, second_poly_hul)

    check(ans, ans1)

def naive_algorithm(first_poly_hul, second_poly_hul):

    points = list(first_poly_hul)
    points += second_poly_hul


    ans = [];

    for p1 in first_poly_hul:
        for p2 in second_poly_hul:
            t1 = list(p1)
            t2 = list(p2)
            t1[0] += 0.00001
            t2[0] -= 0.00001
            intersect = False

            for i in range(len(first_poly_hul) - 1):
                if intersect_line(t1, t2, first_poly_hul[i], first_poly_hul[i + 1]):
                    intersect = True
            if intersect_line(t1, t2, first_poly_hul[-1], first_poly_hul[0]):
                intersect = True

            for i in range(len(second_poly_hul) - 1):
                if intersect_line(t1, t2, second_poly_hul[i], second_poly_hul[i + 1]):
                    intersect = True
            if intersect_line(t1, t2, second_poly_hul[-1], second_poly_hul[0]):
                intersect = True

            if not intersect:
                ans.append([t1, t2])

    return ans


