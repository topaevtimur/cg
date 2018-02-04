

def createSP(plt):
    fig = plt.figure(figsize=(6, 6))
    ax1 = plt.subplot(111, aspect='equal')
    ax1.set_xlim(-5,45)
    ax1.set_ylim(-5,25)
    return fig, ax1