from math import sqrt, ceil
import sys

if __name__ == "__main__":
    seq = set(eval(input()))

    m = max(seq)

    n = 0
    seq1 = set()

    for i in range(1, ceil(sqrt(m))):
        i2 = i * i
        for j in range(i, ceil(sqrt(m - i2)) + 1):
            j2 = j * j
            if i2 + j2 > m:
                break
            for k in range(j, ceil(sqrt(m - i2 - j2)) + 1):
                s = i2 + j2 + k * k
                if s > m:
                    break

                if s in seq and s not in seq1:
                    n += 1
                    seq1.add(s)

                if n >= len(seq):
                    print(n)
                    sys.exit(0)
    print(n)
