class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0

        heights_sorted = sorted(heights)

        for i in range(len(heights)):
            if heights_sorted[i] != heights[i]:
                res += 1
        
        return res
