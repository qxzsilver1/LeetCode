class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        count = [0] * 10001
        n, m = len(mat), len(mat[0])

        for j in range(m):
            for i in range(n):
                count[mat[i][j]] += 1
                if count[mat[i][j]] == n:
                    return mat[i][j]

        return -1
