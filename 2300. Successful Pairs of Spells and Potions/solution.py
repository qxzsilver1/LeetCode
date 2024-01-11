class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = [0] * len(spells)

        for i in range(len(spells)):
            l, r = 0, len(potions) - 1
            idx_leftmost = len(potions)

            while l <= r:
                m = l + (r - l) // 2

                if spells[i] * potions[m] >= success:
                    r = m - 1
                    idx_leftmost = m
                else:
                    l = m + 1
            
            output[i] = len(potions) - idx_leftmost
        
        return output
