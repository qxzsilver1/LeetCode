class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        longest = -1

        for i in range(min(len(s1), len(s2), len(s3))):
            if not s1[i] == s2[i] == s3[i]:
                break
            else:
                longest = i
        
        if longest < 0:
            return -1
        

        longest += 1

        return len(s1) + len(s2) + len(s3) - 3 * longest
