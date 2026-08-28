class NumMatrix:

    def least_significant_bit(self, n: int) -> int:
        return (n & (-n))
    
    def updateBIT(self, r: int, c: int, val: int) -> None:
        i = r
        
        while i <= self.ROWS:
            j = c
            
            while j <= self.COLS:
                self.BIT[i][j] += val

                j += self.least_significant_bit(j)
            i += self.least_significant_bit(i)
    
    def queryBIT(self, r: int, c: int) -> int:
        curr_sum = 0

        i = r

        while i > 0:
            j = c
            
            while j > 0:
                curr_sum += self.BIT[i][j]

                j -= self.least_significant_bit(j)
            i -= self.least_significant_bit(i)
        
        return curr_sum
    
    def buildBIT(self, matrix: List[List[int]]) -> None:
        for i in range(1, self.ROWS + 1):
            for j in range(1, self.COLS + 1):
                val = matrix[i - 1][j - 1]
                self.updateBIT(i, j, val)

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        
        self.COLS = len(matrix[0])

        self.BIT = [[0] * (self.COLS + 1) for _ in range(self.ROWS + 1)]

        self.buildBIT(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        old_val = self.sumRegion(row, col, row, col)
        row += 1
        col += 1

        diff = val - old_val
        self.updateBIT(row, col, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        a = self.queryBIT(row2, col2)
        b = self.queryBIT(row1 - 1, col1 - 1)
        c = self.queryBIT(row2, col1 - 1)
        d = self.queryBIT(row1 - 1, col2)

        return (a + b) - (c + d)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
