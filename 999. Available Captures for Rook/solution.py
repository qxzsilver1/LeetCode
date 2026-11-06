class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        n = len(board)

        r, c = -1, -1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'R':
                    r, c = i, j
        
        res = 0

        curr_r, curr_c = r, c

        while 0 <= curr_r:
            curr_r -= 1

            if curr_r < 0 or board[curr_r][curr_c] == 'B':
                break

            if board[curr_r][curr_c] == 'p':
                res += 1
                break
            else:
                continue
        
        curr_r = r

        while curr_r < n:
            curr_r += 1

            if curr_r == n or board[curr_r][curr_c] == 'B':
                break
            
            if board[curr_r][curr_c] == 'p':
                res += 1
                break
            else:
                continue
        
        curr_r = r

        while 0 <= curr_c:
            curr_c -= 1

            if curr_c < 0 or board[curr_r][curr_c] == 'B':
                break

            if board[curr_r][curr_c] == 'p':
                res += 1
                break
            else:
                continue
        
        curr_c = c
            
        while curr_c < n:
            curr_c += 1

            if curr_c == n or board[curr_r][curr_c] == 'B':
                break
            
            if board[curr_r][curr_c] == 'p':
                res += 1
                break
            else:
                continue
        
        return res
