class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        mod = 10 ** 9 + 7

        # use state rep
        # 5: can't move
        # index 0: 0: 1 bottom element in group - has 2 moves to left (4) or right (6)
        # index 1: 1, 3, 7, 9: 4 diagonals in group: each can move to 2 parts of 2, 4, 6, 8 (each half)
        # index 2: 2, 8: 2 top/bottom group: each can move to 2 diagonals, 7/9 or 1/3
        # index 3: 4, 6: 2 left/right group: each can move to diagonals 3/9 or 1/7, or to 0

        jumps = [1, 4, 2, 2]

        for i in range(n-1):
            tmp = [0] * 4
            tmp[0] = jumps[3]
            tmp[1] = 2 * jumps[2] + 2 * jumps[3]
            tmp[2] = jumps[1]
            tmp[3] = 2 * jumps[0] + jumps[1]
            jumps = tmp
        
        res = 0

        for i in range(len(jumps)):
            res = (res + jumps[i]) % mod
        
        return res
