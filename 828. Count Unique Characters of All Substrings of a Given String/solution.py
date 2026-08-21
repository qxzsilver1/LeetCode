class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)

        idx = collections.defaultdict(list)
        peek = collections.defaultdict(int)

        for i, c in enumerate(s):
            idx[c].append(i)
        
        for c in idx:
            idx[c].extend([n, n])
        
        def get(c):
            return idx[c][peek[c] + 1] - idx[c][peek[c]]
        
        res = 0

        curr = sum(get(c) for c in idx)

        for i, c in enumerate(s):
            res += curr

            old_v = get(c)

            peek[c] += 1
            curr += get(c) - old_v
        
        return res
