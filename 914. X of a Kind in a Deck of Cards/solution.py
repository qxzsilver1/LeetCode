class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count_vals = Counter(deck).values()
        return reduce(gcd, count_vals) >= 2
