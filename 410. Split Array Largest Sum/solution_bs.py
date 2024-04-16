class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def can_split(largest):
            num_subarrays = 0
            curr_sum = 0

            for n in nums:
                curr_sum += n

                if curr_sum > largest:
                    num_subarrays += 1
                    curr_sum = n
            
            return num_subarrays + 1 <= k

        while l <= r:
            m = l + (r - l) // 2

            if can_split(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
