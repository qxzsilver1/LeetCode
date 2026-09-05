class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        running_sum = 0
        points = 0

        for i in range(len(calories)):
            if i <= k - 1:
                running_sum += calories[i]
                continue
            
            if running_sum < lower:
                points -= 1
            elif running_sum > upper:
                points += 1
            
            running_sum -= calories[i - k]
            running_sum += calories[i]
        
        if running_sum < lower:
                points -= 1
        elif running_sum > upper:
            points += 1
        
        return points
