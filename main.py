import ecurve as ec
import numpy as np
import itertools as it


E = ec.ECurve(p=31, a=-3, b=1)

P = E.point(12, 22)
Q = E.point(12, 22)

R, m = P ** 2
print(f'P**2 = {-R}, m = {m}')
