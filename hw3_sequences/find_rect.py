def count_rect(matrix):
    cnt = 0
    for i in range(len(matrix) - 1):
        for j in range(1, len(matrix[0])):
            if (matrix[i][j] == "#" and matrix[i + 1][j] in [".", "-"] and matrix[i][j - 1] == "."):
                cnt += 1
    return cnt


dash_line = 0
matrix = []
while True:
    data = input()
    if "-" in data:
        dash_line += 1
        if dash_line == 2:
            matrix.append(data)
            break
    else:
        matrix.append(data)

cnt = count_rect(matrix)
print(cnt)
