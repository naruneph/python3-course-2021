from math import log, sqrt
try:
    num = int(input())
    if 2 <= num <= 1000000:
        for i in range(2, int(sqrt(num))+1):
            p = i
            while p < num:
                p *= i
            if p == num:
                print("YES")
                break
        else:
            print("NO")
    else:
        raise ValueError
except Exception:
    print("WRONG INPUT")
