class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n = len(picture)
        m = len(picture[0])

        row_cnt = [0] * n
        col_cnt = [0] * m

        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B':
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        
        res = 0

        for i in range(n):
            for j in range(m):
                if picture[i][j] == 'B' and row_cnt[i] == 1 and col_cnt[j] == 1:
                    res += 1
        
        return res
