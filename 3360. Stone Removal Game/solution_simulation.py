class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        k = 0

        while n >= take:
            n -= take
            take -= 1
            k += 1
        
        return k % 2 == 1
