class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        contiguous_empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((contiguous_empty - 1) / 2) # round int division towards 0 - python
                contiguous_empty = 0
            else:
                contiguous_empty += 1
        
        n -= (contiguous_empty) // 2 
        
        return n <= 0
