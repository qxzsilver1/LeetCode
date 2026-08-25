class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0

        for i in range(128):
            if count > 1:
                break

            cnt = 0

            for j in range(len(s)):
                if s[j] == chr(i):
                    cnt += 1
            
            count += cnt % 2
        
        return count <= 1
