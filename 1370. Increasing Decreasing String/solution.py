class Solution:
    def sortString(self, s: str) -> str:
        res = []
        counter = Counter(s)

        while len(res) < len(s):
            for seq in [string.ascii_lowercase, string.ascii_lowercase[::-1]]:
                for c in seq:
                    if counter[c] > 0:
                        res.append(c)
                        counter[c] -= 1
        
        return ''.join(res)
