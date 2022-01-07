from fractions import Fraction
from math import floor


class Sausage:
    def __init__(self, stuffling="pork!", volume=1):
        self.stuffling = (stuffling * int(12/len(stuffling) + 1))[:12]
        self.volume = Fraction(volume)

    def __repr__(self):
        result = ""

        full_parts = floor(self.volume)
        last_part = self.volume - full_parts

        # top
        result += ("/" + "-" * 12 + "\\") * full_parts
        if last_part > 0 or self.volume == 0:
            result += "/" + "-" * int(12 * last_part) + "|"
        result += "\n"

        # center
        for _ in range(3):
            result += ("|" + self.stuffling + "|") * full_parts
            if last_part > 0 or self.volume == 0:
                result += "|" + self.stuffling[:int(12 * last_part)] + "|"
            result += "\n"

        # bottom
        result += ("\\" + "-" * 12 + "/") * full_parts
        if last_part > 0 or self.volume == 0:
            result += "\\" + "-" * int(12 * last_part) + "|"

        return result

    def __mul__(self, n):
        return Sausage(self.stuffling, self.volume * n)

    def __rmul__(self, n):
        return Sausage(self.stuffling, self.volume * n)

    def __truediv__(self, n):
        return Sausage(self.stuffling, self.volume / Fraction(n))

    def __add__(self, other):
        return Sausage(self.stuffling, self.volume + other.volume)

    def __sub__(self, other):
        new_vol = self.volume - other.volume
        return Sausage(self.stuffling, new_vol if new_vol >= 0 else 0)

    def __abs__(self):
        return self.volume

    def __bool__(self):
        return bool(self.volume)
