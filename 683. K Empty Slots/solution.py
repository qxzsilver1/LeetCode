class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * n

        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day
        
        res = n + 1
        l, r = 0, k + 1

        while r < n:
            i = l + 1

            while i < r and days[i] > days[l] and days[i] > days[r]:
                i += 1
            
            if i == r:
                res = min(res, max(days[l], days[r]))
            
            l = i
            r = l + k + 1
        
        return -1 if res == n + 1 else res
