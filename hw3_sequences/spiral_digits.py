def counter():
    i = 0
    while True:
        yield i
        i = (i + 1) % 10


def make_spiral(cols, rows):
    spiral = [[-1 for _ in range(cols)] for _ in range(rows)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r = 0
    c = 0
    d = 0
    val = counter()
    for _ in range(cols * rows):
        spiral[r][c] = next(val)

        possible_r = r + dirs[d][0]
        possible_c = c + dirs[d][1]

        if (possible_r, possible_c) in [
            (0, cols - 1),
            (rows - 1, cols - 1),
            (rows - 1, 0),
        ]:
            r = possible_r
            c = possible_c
            d = (d + 1) % 4

        elif possible_r < rows and possible_c < cols:
            if spiral[possible_r][possible_c] != -1:
                d = (d + 1) % 4
                r += dirs[d][0]
                c += dirs[d][1]

            else:
                r = possible_r
                c = possible_c

        else:
            d = (d + 1) % 4
            r += dirs[d][0]
            c += dirs[d][1]

    return spiral


def draw_spiral(spiral):
    for row in spiral:
        print(*row)


cols, rows = eval(input())
spiral = make_spiral(cols, rows)
draw_spiral(spiral)
