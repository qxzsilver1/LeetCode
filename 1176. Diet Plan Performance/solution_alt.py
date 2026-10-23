class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        total = score = 0
        
        for i, value in enumerate(calories):
            total += value
            
            if i >= k:
                total -= calories[i - k]
            
            if i >= k - 1:
                score += int(total > upper) - int(total < lower)
        
        return score
