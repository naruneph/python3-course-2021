def divdigit(N):
    digits = [str(d) for d in range(1, 10) if N % d == 0]
    cnt = 0
    for d in str(N):
        if d in digits:
            cnt += 1
    return cnt
