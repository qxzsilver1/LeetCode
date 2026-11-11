class Solution:
    def minSwaps(self, data: list[int]) -> int:
        k = sum(data)

        already_inside = sum(data[:k])

        best = already_inside

        for start in range(1, len(data) - k + 1):
            already_inside += data[start + k - 1] - data[start - 1]
            best = max(best, already_inside)
        
        return k - best
