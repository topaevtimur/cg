

def hullGo (hull, ax, poly_np, poly) :
    tmp_poly_hul = []
    for simplex in hull.simplices:
        ax.plot(poly_np[simplex, 0], poly_np[simplex, 1], 'k-')
    for v in hull.vertices:
        tmp_poly_hul.append(poly[v])

    return tmp_poly_hul, ax