from math import sqrt
try:
    x, y, r = [float(i) for i in input().split(",")]
    if r < 0:
        raise ValueError
    dots_in_circle = True
    while True:
        dot_x, dot_y = [float(i) for i in input().split(",")]
        if (dot_x, dot_y) == (0.0, 0.0):
            print("YES") if dots_in_circle else print("NO")
            break
        else:
            check_result = sqrt(((x - dot_x)**2 + (y - dot_y)**2)) <= r
            dots_in_circle = dots_in_circle and check_result
except Exception:
    print("WRONG INPUT")
