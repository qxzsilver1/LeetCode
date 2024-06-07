class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        l, r = 0, n - 1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        i = 0

        for j in range(n + 1):
            if j == n or s[j] == ' ':
                l, r = i, j - 1

                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                
                i = j + 1
