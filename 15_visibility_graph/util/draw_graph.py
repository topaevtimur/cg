from IPython.display import display


def drawGraph(ans, ax1, fig) :
    for v in ans:
        p1 = v[0]
        p2 = v[1]
        ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color='r', linestyle='-', linewidth=1)

    display(fig)