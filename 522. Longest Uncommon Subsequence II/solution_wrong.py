class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        return -1 if any(a == b for a, b in zip(strs, strs[1:])) else max(len(a) for a in strs)
