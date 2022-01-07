import sys
from collections import defaultdict


def read_tunnel_info(f):
    inf = defaultdict(set)
    start_end = []

    for info in f:
        info = info.split()
        if len(info) == 2:
            inf[info[0]].add(info[1])
            inf[info[1]].add(info[0])
        else:
            start_end.append(info[0])

    if len(start_end) != 2:
        raise ValueError("start or end not provided")
    return inf, start_end[0], start_end[1]


def bfs(inf, s, e):
    visited = {s}
    q = [s]

    while len(q) > 0:
        elem = q.pop()
        if elem == e:
            return True
        q += inf[elem] - visited
        visited |= inf[elem]

    return False


if __name__ == "__main__":
    tunnel_info, start, end = read_tunnel_info(sys.stdin)
    if bfs(tunnel_info, start, end):
        print("YES")
    else:
        print("NO")
