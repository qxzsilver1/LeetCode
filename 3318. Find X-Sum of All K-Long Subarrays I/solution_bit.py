class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        g = n - k + 1
        ans = [0] * g
        freq = [0] * 51

        for i in range(k):
            freq[nums[i]] += 1

        best = [0] * x  # packed key = (freq << 6) | value
        SHIFT = 6
        MASK = (1 << SHIFT) - 1

        def xsum():
            filled = 0
            # build top-x descending by one-pass insertion
            for v in range(1, 51):
                f = freq[v]
                if not f:
                    continue
                key = (f << SHIFT) | v
                if filled < x:
                    j = filled
                    while j > 0 and key > best[j - 1]:
                        best[j] = best[j - 1]
                        j -= 1
                    best[j] = key
                    filled += 1
                else:
                    if key <= best[x - 1]:
                        continue
                    j = x - 1
                    while j > 0 and key > best[j - 1]:
                        best[j] = best[j - 1]
                        j -= 1
                    best[j] = key

            s = 0
            take = filled if filled < x else x
            for i in range(take):
                key = best[i]
                s += (key >> SHIFT) * (key & MASK)
            return s

        ans[0] = xsum()

        for i in range(1, g):
            freq[nums[i - 1]] -= 1
            freq[nums[i + k - 1]] += 1
            ans[i] = xsum()

        return ans

