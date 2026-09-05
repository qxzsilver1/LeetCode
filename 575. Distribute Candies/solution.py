class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_types = set()
        n = len(candyType)
        num_can_eat = n // 2

        for c in candyType:
            if c not in candy_types:
                candy_types.add(c)
        
        return min(len(candy_types), num_can_eat)
