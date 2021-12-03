import ecurve as ec

E = ec.ECurve(p=31, a=-3, b=1)

P = E.point(12, 22)
Q = E.point(13, 19)

R, m = P + Q
print(f'P + Q = {-R}, m = {m}') # P + Q = (15, 18), m = 28

R, m = P ** 2
print(f'P**2 = {-R}, m = {m}') # P ** 2 = (11, 11), m = 2
