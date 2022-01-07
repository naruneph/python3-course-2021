def frange(x, y, jump):
    while x <= y:
        yield x
        x += jump


class Dots:
    def __init__(self, begin, end):
        self.begin = float(begin)
        self.end = float(end)

    def __getitem__(self, item):

        if isinstance(item, int):
            start = self.begin
            stop = self.end
            jump = abs(self.end - self.begin) / (item - 1)

            return frange(start, stop, jump)

        elif isinstance(item, slice):
            i = item.start
            n = item.stop
            step = item.step

            if step is None:

                if i < 0:
                    jump = (self.end - self.begin) / (n - 1)
                    start = self.begin + jump * i
                    # stop = self.end
                    i = 0
                else:
                    if i < n:
                        start = self.begin
                        # stop = self.end
                        jump = (self.end - self.begin) / (n - 1)
                    else:
                        jump = (self.end - self.begin) / (n - 1)
                        start = self.begin
                        # stop = self.end + jump * (i - n + 1)

                return start + jump * i

            else:
                jump = (self.end - self.begin) / (step - 1)

                if i is None:
                    start = self.begin
                    i = 0
                else:
                    start = self.begin + jump * i
                    if i < 0:
                        i = 0

                if n is None:
                    stop = self.end
                else:
                    stop = self.begin + jump * (n - 1)

                return frange(start, stop, jump)
