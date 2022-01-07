class WeAre:
    count = 0

    def __init__(self):
        WeAre.count += 1

    def __del__(self):
        WeAre.count -= 1


# a = WeAre()
# print(a.count)
# b, c = WeAre(), WeAre(),
# print(a.count, b.count, c.count)
# del b
# print(a.count)
