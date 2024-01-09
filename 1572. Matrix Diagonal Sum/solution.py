class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        mid = 0

        for i in range(n):
            sum += (mat[i][i] + mat[i][n-1-i])
        
        return sum if n % 2 == 0 else sum - mat[n // 2][n // 2]
