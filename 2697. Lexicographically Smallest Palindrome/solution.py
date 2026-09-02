class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r = 0, len(s) - 1

        res = list(s)

        while l < r:
            if res[l] < res[r]:
                res[r] = res[l]
            else:
                res[l] = res[r]

            l += 1
            r -= 1
        
        return ''.join(res)
