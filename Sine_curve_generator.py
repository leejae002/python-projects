import matplotlib.pyplot as plt
import math
import numpy

sin_pts = []
x_pts = numpy.arange(0, 10, 0.01)

def sin_graph(amp):
    for x in x_pts:
        sin_pts.append(amp * math.sin(x))
    plt.plot(x_pts, sin_pts)
    plt.show()

sin_graph(4)
