class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10 ** 9 + 7
        
        def countAndSum(nums, n, target):
            count = 0
            curr_sum, total_sum, window_sum = 0, 0, 0

            i = 0

            for j in range(n):
                curr_sum += nums[j]
                window_sum += nums[j] * (j - i + 1)

                while curr_sum > target:
                    window_sum -= curr_sum
                    curr_sum -= nums[i]

                    i += 1
                
                count += j - i + 1
                total_sum += window_sum
            
            return count, total_sum
        
        def sumOfFirstK(nums, n, k):
            min_sum, max_sum = min(nums), sum(nums)

            l, r = min_sum, max_sum

            while l <= r:
                m = l + (r - l) // 2

                if countAndSum(nums, n, m)[0] >= k:
                    r = m - 1
                else:
                    l = m + 1
            
            count, total_sum = countAndSum(nums, n, l)

            return total_sum - l * (count - k)
        
        res = (sumOfFirstK(nums, n, right) - sumOfFirstK(nums, n, left - 1)) % mod

        return (res + mod) % mod
