class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = Counter(s)

        odd_max = 0
        even_min = len(s)

        for cnt in frequency.values():
            if cnt & 1:
                odd_max = max(odd_max, cnt)
            else:
                even_min = min(even_min, cnt)
        
        return odd_max - even_min
