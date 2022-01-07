def solve(k):
    if k == 0:
        return 0
    dig = k
    carry = 0
    num = k
    magnitude = 1

    while dig != 1 or carry != 0:
        magnitude *= 10

        val = dig * k + carry
        dig = val % 10
        carry = val // 10
        num = dig * magnitude + num

    return num


if __name__ == "__main__":
    k = int(input())
    print(solve(k))
