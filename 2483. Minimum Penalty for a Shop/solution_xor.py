class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty, earliest_idx = float('inf'), 0

        for i in range(-1, len(customers)):
            penalty_sum = 0
            for j in range(len(customers)):
                if i < 0:
                    penalty_sum += 1 if customers[j] != 'N' else 0
                else:
                    if j <= i:
                        penalty_sum += 1 if customers[j] != 'Y' else 0
                    else:
                        penalty_sum += 1 if customers[j] != 'N' else 0
            
            if penalty_sum < min_penalty:
                earliest_idx = i + 1
                min_penalty = penalty_sum
        
        return earliest_idx

                    
