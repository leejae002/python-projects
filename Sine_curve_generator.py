import matplotlib.pyplot as plt
import math
import numpy

sin_pts = []

for x in numpy.arange(0, 10, 0.01):
    sin_pts.append(math.sin(x))

plt.plot( sin_pts)
plt.axis([0, 10, -2, 2])
plt.show()


