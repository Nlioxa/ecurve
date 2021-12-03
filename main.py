import ecurve as ec
import numpy as np
import itertools as it


E = ec.ECurve(p=31, a=-3, b=1)

P = E.point(12, 22)
Q = E.point(12, 22)

res, m = P ** 2
b = P.y - m * P.x

x, y = np.ogrid[0 : E.ff.p, 0 : E.ff.p]

points = np.array([
    point
    for point in it.product(x.ravel(), y.ravel())
    if E.on_curve(point[0], point[1])
])

xs = points[:,0]
ys = points[:,1]

ys_pq = [int(E.ff(i)) for i in (int(m) * x + int(b))]
xs_pq = list(x.squeeze())