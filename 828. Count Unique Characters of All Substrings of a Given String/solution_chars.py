class Solution:
    def uniqueLetterString(self, s: str) -> int:
        idx = collections.defaultdict(list)
        
        for i, c in enumerate(s):
            idx[c].append(i)
        
        res = 0

        for a in idx.values():
            a = [-1] + a + [len(s)]

            for i in range(1, len(a) - 1):
                res += (a[i] - a[i-1]) * (a[i+1] - a[i])
        
        return res
