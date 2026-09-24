class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
            rows, cols = len(matrix), len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]
            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        A = compress_matrix(mat1)
        B = compress_matrix(mat2)

        res = [[0] * n for _ in range(m)]

        for mat1_row in range(m):
            # Iterate on all current 'row' non-zero elements of mat1.
            for element1, mat1_col in A[mat1_row]:
                # Multiply and add all non-zero elements of mat2
                # where the row is equal to col of current element of mat1.
                for element2, mat2_col in B[mat1_col]:
                    res[mat1_row][mat2_col] += element1 * element2

        return res
