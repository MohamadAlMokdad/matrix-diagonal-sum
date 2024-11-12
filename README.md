# 🔢 Matrix Diagonal Sum

This Python function calculates the sum of the main diagonal elements (top-left to bottom-right) in a square matrix.

## 📜 Function: `matrix_diagonal_sum`

### 📝 Description
The `matrix_diagonal_sum` function iterates through a square matrix and sums up the elements along the main diagonal, which is made up of elements positioned at `(0, 0)`, `(1, 1)`, `(2, 2)`, etc.

# 🎉 Example:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = matrix_diagonal_sum(matrix)
print(result)  # Output: 15 (1 + 5 + 9)
