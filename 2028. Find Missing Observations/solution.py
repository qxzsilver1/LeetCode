class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_sum = mean * (len(rolls) + n) - sum(rolls)

        if missing_sum > 6 * n or missing_sum < n:
            return []
        
        target = missing_sum // n

        if target == missing_sum / n:
            return [target] * n
        else:
            res = [target] * n
            remaining = missing_sum - target * n

            i = 0
            while remaining and i < n:
                val_to_add = min(6 - res[i], remaining)
                res[i] += val_to_add
                remaining -= val_to_add
                i += 1
            
            return res


