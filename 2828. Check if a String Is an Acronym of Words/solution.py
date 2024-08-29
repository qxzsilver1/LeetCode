class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        p1, p2 = 0, 0

        while p1 < len(words) and p2 < len(s) and words[p1][0] == s[p2]:
            p1 += 1
            p2 += 1
        
        return len(words) == p2 == len(s)
