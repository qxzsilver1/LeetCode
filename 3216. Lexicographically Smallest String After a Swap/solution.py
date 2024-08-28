class Solution:
    def getSmallestString(self, s: str) -> str:
        res = list(s)

        for i in range(1, len(s)):
            prev, curr = int(s[i-1]), int(s[i])

            if curr < prev and prev % 2 == curr % 2:
                res[i], res[i-1] = res[i-1], res[i]
                break
        
        return ''.join(res)
