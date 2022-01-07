N, M = (int(i) for i in input().replace(" ", "").split(","))

max_len_factors = len(str(N))
max_len_product = len(str(N * N))

col_len = max_len_factors * 2 + 3 + 3 + max_len_product
delim_len = 3

col_num = N
col_num_for_row = M // (col_len + delim_len)
if col_num_for_row * (col_len + delim_len) + col_len < M:
    col_num_for_row += 1

row_num = col_num // col_num_for_row
if col_num % col_num_for_row != 0:
    row_num += 1

for rn in range(row_num):
    print("=" * M)
    for j in range(1, N + 1):
        i_from = 1 + col_num_for_row * rn
        i_to = min(col_num_for_row * (rn + 1) + 1, N + 1)
        for i in range(i_from, i_to):
            if i == i_to - 1:
                print(
                    f"{i:{' '}{'>'}{max_len_factors}} * {j:{' '}{'<'}{max_len_factors}} = {i*j:{' '}{'<'}{max_len_product}}",
                    end="",
                )
            else:
                print(
                    f"{i:{' '}{'>'}{max_len_factors}} * {j:{' '}{'<'}{max_len_factors}} = {i*j:{' '}{'<'}{max_len_product}}",
                    end=" | ",
                )
        print()

print("=" * M)
