class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        indegrees = [0] * n

        for i in range(n):
            for j in range(n):
                indegrees[i] += matrix[i][j]
        
        return indegrees
