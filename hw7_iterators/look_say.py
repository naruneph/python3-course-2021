def LookSay():
    prev_number = "1"
    s = 1

    yield 1

    while True:
        x = prev_number + ' '
        prev_number = ''

        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                s += 1
            else:
                yield s
                yield int(x[i])

                prev_number += str(s) + x[i]
                s = 1

        x = ''
        s = 1
