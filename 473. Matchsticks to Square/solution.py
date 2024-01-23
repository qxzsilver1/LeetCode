class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        avg_lengths = sum(matchsticks) // 4

        if sum(matchsticks) / 4 != avg_lengths:
            return False
        
        sides = [0] * 4

        matchsticks.sort(reverse=True) # greedy algorithm - start with largest matches first

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(len(sides)):
                if sides[j] + matchsticks[i] <= avg_lengths:
                    sides[j] += matchsticks[i]
                    
                    if backtrack(i + 1):
                        return True
                    
                    sides[j] -= matchsticks[i]
            
            return False
        
        return backtrack(0)
