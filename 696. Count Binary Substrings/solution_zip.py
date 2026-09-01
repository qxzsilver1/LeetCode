class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(v)) for _, v in itertools.groupby(s)]

        return sum((min(a, b) for a, b in zip(groups, groups[1:])))
