import ffield as ff

class ECurve:
    def __init__(self, p, a:int=0, b:int=0):
        self.ff = ff.FField(p)
        self.a = a
        self.b = b

    def __str__(self):
        return f'ECurve(F = {self.ff}, a = {self.a}, b = {self.b})'

    def __repr__(self):
        return f'ECurve(F = {self.ff}, a = {self.a}, b = {self.b})'

    def __call__(self, x):
        y_sq = self.ff(x) ** 3 + self.a * self.ff(x) + self.b
        for i in range(self.ff.p):
            res = self.ff(i)
            if res**2 == y_sq:
                return res
        raise ValueError(
            f"P(x = {int(x)}, y - ?) does't have a 'y' on the curve"
        )

    def on_curve(self, x, y):
        return self.ff(y) ** 2 == self.ff(x) ** 3 + self.ff(x) * self.a + self.b

    def point(self, x, y):
        return EPoint(self, x, y)

    def add_points(self, p: tuple, q: tuple):
        x_p, y_p = p
        x_q, y_q = q
        ###
        # P != Q
        #
        if x_p != x_q or y_p != y_q:
            m = (y_p - y_q) / (x_p - x_q)
        #
        # P == Q
        #
        else:
            m = (x_p**2*3 + self.a) / (y_p*2)
        ###
        # x_
        #
        x_r = (m**2 - x_p - x_q)
        y_r = (y_q + m*(x_r - x_q))

        return x_r, y_r, m

class EPoint:
    def __init__(self, ec: ECurve, x=0, y=0):
        self.ec = ec
        self.x = ec.ff(x)
        self.y = ec.ff(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'EPoint({self.x}, {self.y})'

    def __eq__(self, othr):
        return self.x == othr.x and self.y == othr.y

    def __add__(self, othr):
        R = EPoint(self.ec)
        
        if self != othr:
            m = (self.y - othr.y) / (self.x - othr.x)
        else:
            m = (self.x**2*3 + self.ec.a) / (self.y*2)

        R.x = (m**2 - self.x - othr.x)
        R.y = (self.y + m*(R.x - self.x))

        return R, m

    def __pow__(self, p):
        if p > 0:
            res = self
            m = 0
            for i in range(p - 1):
                res, m = res + res
            return res, m
        else:
            raise ValueError('p must be positive integer')

    def __neg__(self):
        return EPoint(self.ec, self.x, -self.y)
