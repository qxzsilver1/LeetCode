class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        val_count = defaultdict(int)
        n = len(nums)

        curr_sum, max_sum = 0, 0

        for i in range(k):
            curr_sum += nums[i]
            val_count[nums[i]] += 1
        
        if len(val_count) == k:
            max_sum = curr_sum
        
        for i in range(k, n):
            curr_sum -= nums[i-k]
            val_count[nums[i-k]] -= 1

            if val_count[nums[i-k]] == 0:
                del val_count[nums[i-k]]
            
            curr_sum += nums[i]
            val_count[nums[i]] += 1

            if len(val_count) == k:
                max_sum = max(max_sum, curr_sum)
        
        return max_sum
