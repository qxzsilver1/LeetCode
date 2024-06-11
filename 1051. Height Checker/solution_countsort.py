class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0

        count = [0] * 101

        for h in heights:
            count[h] += 1
        
        expected = []

        for h in range(1, 101):
            c = count[h]

            for _ in range(c):
                expected.append(h)

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res += 1
        
        return res
