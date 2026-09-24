class SparseMatrix:
    def __init__(self, matrix: List[List[int]], col_wise: bool):
        self.values, self.row_index, self.col_index = self.CompressMatrix(matrix, col_wise)

    def CompressMatrix(self, matrix: List[List[int]], col_wise: bool):
        return self.CompressByCol(matrix) if col_wise else self.CompressByRow(matrix)

    # Compressed Sparse Row
    def CompressByRow(self, matrix: List[List[int]]):
        values = []
        row_index = [0]
        col_index = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    col_index.append(col)
            row_index.append(len(values))

        return values, row_index, col_index

    # Compressed Sparse Column
    def CompressByCol(self, matrix: List[List[int]]):
        values = []
        row_index = []
        col_index = [0]

        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    row_index.append(row)
            col_index.append(len(values))

        return values, row_index, col_index

class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        A = SparseMatrix(mat1, False)
        B = SparseMatrix(mat2, True)

        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for row in range(len(res)):
            for col in range(len(res[0])):

                # Row element range indices
                mat1_row_start = A.row_index[row]
                mat1_row_end = A.row_index[row + 1]

                # Column element range indices
                mat2_col_start = B.col_index[col]
                mat2_col_end = B.col_index[col + 1]

                # Iterate over both row and column.
                while mat1_row_start < mat1_row_end and mat2_col_start < mat2_col_end:
                    if A.col_index[mat1_row_start] < B.row_index[mat2_col_start]:
                        mat1_row_start += 1
                    elif A.col_index[mat1_row_start] > B.row_index[mat2_col_start]:
                        mat2_col_start += 1
                    # Row index and col index are same so we can multiply these elements.
                    else:
                        res[row][col] += A.values[mat1_row_start] * B.values[mat2_col_start]
                        mat1_row_start += 1
                        mat2_col_start += 1

        return res
