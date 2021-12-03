def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """

    def extended_euclidean_algorithm(a, b):
        """
        Returns a three-tuple (gcd, x, y) such that
        a * x + b * y == gcd, where gcd is the greatest
        common divisor of a and b.

        This function implements the extended Euclidean
        algorithm and runs in O(log b) in the worst case.
        """
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = b, a

        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return old_r, old_s, old_t

    gcd, x, y = extended_euclidean_algorithm(n, p)

    if gcd != 1 or (n * x + p * y) % p != gcd:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            f"{n} has no multiplicative inverse \
              modulo {p}"
        )
    else:
        return x % p

class FField:
    def __init__(self, p: int = 1):
        self.p = p

    def __call__(self, num=0):
        return FNumber(self, int(num))

    def __str__(self):
        return f"F({self.p})"

    def __repr__(self):
        return f"FField({self.p})"

    def add(self, lhs, rhs):
        return self(int(lhs) + int(rhs))

    def add_inv(self, num):
        return self(-int(num))

    def sub(self, lhs, rhs):
        return self.add(int(lhs), -int(rhs))

    def mul(self, lhs, rhs):
        return self(int(lhs) * int(rhs))

    def mul_inv(self, num):
        return self(inverse_of(int(num), self.p))

    def div(self, lhs, rhs):
        return self.mul(lhs, self.mul_inv(rhs))


class FNumber:
    def __init__(self, field: FField, value: int):
        self.ff = field
        self.value = value % field.p

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"FNumber({self.value} mod {self.ff})"

    def __add__(self, num):
        return self.ff.add(self.value, num)

    def __sub__(self, num):
        return self.ff.sub(self.value, num)

    def __mul__(self, num):
        return self.ff.mul(self.value, num)

    def __truediv__(self, num):
        return self.ff.div(self.value, num)

    def __pow__(self, num):
        res = self
        for _ in range(int(num) - 1):
            res = res * self
        return self.ff(res)

    def __neg__(self):
        return self.ff.add_inv(self)

    def __mod__(self, value):
        return self.ff(self.value % value)

    def __eq__(self, num):
        return int(self) == int(num)

    def inv(self):
        return self.ff.mul_inv(self)

    def int(self):
        return self.value
