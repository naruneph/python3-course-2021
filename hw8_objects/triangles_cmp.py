from math import sqrt


class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = float(s1)
        self.s2 = float(s2)
        self.s3 = float(s3)

    def __bool__(self):
        return not (
            self.s1 <= 0 or
            self.s2 <= 0 or
            self.s3 <= 0 or
            self.s1 + self.s2 <= self.s3 or
            self.s2 + self.s3 <= self.s1 or
            self.s3 + self.s1 <= self.s2
        )

    def __abs__(self):
        if self:
            p = (self.s1 + self.s2 + self.s3) / 2
            return sqrt(p * (p - self.s1) * (p - self.s2) * (p - self.s3))
        else:
            return 0

    def __eq__(self, other):
        return set([self.s1, self.s2, self.s3]) == set([other.s1, other.s2, other.s3])

    def __ne__(self, other):
        return abs(self) != abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __repr__(self):
        return f"{self.s1}:{self.s2}:{self.s3}"

    def __float__(self):
        return abs(self)
