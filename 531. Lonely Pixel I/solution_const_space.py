class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        def check(x, y):
            n = len(picture)
            m = len(picture[0])

            cnt = 0

            for i in range(n):
                cnt += 1 if picture[i][y] == 'B' else 0
            
            for j in range(m):
                if j != y:
                    cnt += 1 if picture[x][j] == 'B' else 0
            
            return picture[x][y] == 'B' and cnt == 1

        n = len(picture)
        m = len(picture[0])
        
        res = 0

        for j in range(m):
            res += 1 if check(0, j) else 0
        
        for i in range(1, n):
            res += 1 if check (i, 0) else 0
        
        for j in range(m):
            picture[0][j] = '1' if picture[0][j] == 'B' else '0'
        
        for i in range(n):
            picture[i][0] = '1' if picture[i][0] == 'B' else '0'

        for i in range(1, n):
            for j in range(1, m):
                if picture[i][j] == 'B':
                    picture[i][0] = chr(ord(picture[i][0]) + 1)
                    picture[0][j] = chr(ord(picture[0][j]) + 1)

        for i in range(1, n):
            for j in range(1, m):
                if picture[i][j] == 'B':
                    if picture[i][0] == '1' and picture[0][j] == '1':
                        res += 1
        
        return res
