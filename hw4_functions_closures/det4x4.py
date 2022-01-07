def minor(matrix, i, j):
    new_matrix = []
    for row in range(len(matrix)):
        if row != i:
            tmp = []
            for col in range(len(matrix[0])):
                if col != j:
                    tmp.append(matrix[row][col])
            new_matrix.append(tmp)
    return new_matrix


def det(matrix, size):
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        matrix_det = 0
        for j in range(len(matrix[0])):
            matrix_det += (-1)**j * matrix[0][j] * det(minor(matrix, 0, j), size - 1)
        return matrix_det


matrix = eval(input())
print(det(matrix, len(matrix[0])))
