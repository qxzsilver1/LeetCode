class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False

        target = total // k

        nums.sort(reverse=True)
        n = len(nums)

        def backtrack(i, k, subset_sum, bitmask):
            if k == 0:
                return True
            
            if subset_sum == target:
                return backtrack(0, k-1, 0, bitmask)
            
            for j in range(i, n):
                if (bitmask & (1 << j)) == 0 or subset_sum + nums[j] > target:
                    continue

                if backtrack(j + 1, k, subset_sum + nums[j], bitmask ^ (1 << j)):
                    return True

                if subset_sum == 0:
                    return False
            
            return False
        
        return backtrack(0, k, 0, (1 << n) - 1)
