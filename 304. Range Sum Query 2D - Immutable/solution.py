class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum_matrix = [[0] * (cols+1) for r in range(rows + 1)]

        for r in range(rows):
            prefix_sum = 0
            for c in range(cols):
                prefix_sum += matrix[r][c]
                sum_above = self.prefix_sum_matrix[r][c+1]
                self.prefix_sum_matrix[r+1][c+1] = prefix_sum + sum_above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        return self.prefix_sum_matrix[r2][c2] + self.prefix_sum_matrix[r1-1][c1-1] - self.prefix_sum_matrix[r1-1][c2] - self.prefix_sum_matrix[r2][c1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
