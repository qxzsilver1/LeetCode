class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # Greedily pick the larger version of each string
        for i in range(len(strs)):
            rev = strs[i][::-1]
            if rev > strs[i]:
                strs[i] = rev

        res = ""

        for i in range(len(strs)):
            rev = strs[i][::-1]

            # Build the "other" part: everything after i, then before i
            other = "".join(strs[i + 1:]) + "".join(strs[:i])

            # Try both orientations of string i
            for s in (strs[i], rev):
                for j in range(len(s)):
                    candidate = s[j:] + other + s[:j]
                    if candidate > res:
                        res = candidate

        return res
