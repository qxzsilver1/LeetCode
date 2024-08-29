class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        offset = ord('A')

        r1, r2 = int(s[1]), int(s[4])
        c1, c2 = ord(s[0]) - offset, ord(s[3]) - offset

        res = [''] * ((r2 - r1 + 1) * (c2 - c1 + 1))

        for c in range(c1, c2 + 1):

            for r in range(r1, r2 + 1):
                res[((r - r1) + ((c - c1) *(r2 - r1 + 1)))] = chr(c + offset) + str(r) 
        
        return res
