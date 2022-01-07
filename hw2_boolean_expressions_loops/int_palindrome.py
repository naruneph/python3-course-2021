try:
    num = int(input())
    if num < 0:
        raise ValueError
    num_copy = num
    if num % 10 == 0 and num != 0:
        print("NO")
    else:
        reversed_num = 0
        while num:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        if num_copy == reversed_num:
            print("YES")
        else:
            print("NO")
except Exception:
    print("WRONG INPUT")
