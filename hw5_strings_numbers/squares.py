def squares(w, h, *squares):
    minY = h
    minX = w
    maxYs = 1
    maxXs = 1

    for X, Y, s, c in squares:
        if Y < minY:
            minY = Y
        if X < minX:
            minX = X
        if Y + s > maxYs:
            maxYs = Y + s
        if X + s > maxXs:
            maxXs = X + s

    empty_line = "." * w + "\n"
    top_fill = empty_line * minY
    bottom_fill = empty_line * (h - maxYs)
    left_fill = "." * minX
    right_fill = "." * (w - maxXs)

    print(top_fill, end="")

    for hc in range(minY, maxYs):
        print(left_fill, end="")
        for wc in range(minX, maxXs):
            fill_char = "."
            for X, Y, s, c in squares:
                if Y <= hc <= Y + s - 1 and X <= wc <= X + s - 1:
                    fill_char = c

            print(fill_char, end="")
        print(right_fill)

    print(bottom_fill, end="")