import sys
from itertools import product
from math import sqrt


def read_galaxies(f):
    galaxies = []

    for g in f:
        g = g.split()
        if len(g) < 4:
            continue
        x, y, z, n = g
        galaxies.append((n, float(x), float(y), float(z)))

    return galaxies


if __name__ == "__main__":
    galaxies = read_galaxies(sys.stdin)
    max_dist = 0.0
    far_galaxies = None

    for (n1, x1, y1, z1), (n2, x2, y2, z2) in product(galaxies, repeat=2):
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        if dist > max_dist:
            max_dist = dist
            far_galaxies = (n1, n2)

    print(*sorted(far_galaxies))
