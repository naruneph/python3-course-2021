def fuse_segments(segments):
    res = []
    cur_start, cur_end = segments[0]

    for i in range(1, len(segments)):
        if cur_end < segments[i][0]:
            res.append((cur_start, cur_end))
            cur_start, cur_end = segments[i]
        elif cur_end <= segments[i][1]:
            cur_end = segments[i][1]

    if (cur_start, cur_end) not in res:
        res.append((cur_start, cur_end))
    return res


def sum_of_segments(seg):
    seg_sum = 0
    for item in seg:
        seg_sum += item[1] - item[0]
    return seg_sum


segments = sorted(list(eval(input())))
fused_segments = fuse_segments(segments)
print(sum_of_segments(fused_segments))
