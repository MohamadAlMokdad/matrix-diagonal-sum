def matrix_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]  # Add the element at position (i, i)
    return diagonal_sum
