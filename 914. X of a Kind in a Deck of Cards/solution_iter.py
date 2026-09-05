class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnts = Counter(deck)

        n = len(deck)

        for i in range(2, n + 1):
            if n % i == 0:
                if all(v % i == 0 for v in cnts.values()):
                    return True
        
        return False
