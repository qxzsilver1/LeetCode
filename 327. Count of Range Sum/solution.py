class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cum_sum = [0]
        
        for n in nums:
            cum_sum.append(cum_sum[-1] + n)
        
        def mergesort(l, r):
            if l == r:
                return 0
            
            mid = (l + r) // 2

            cnt = mergesort(l, mid) + mergesort(mid + 1, r)

            i = j = mid + 1

            for left in cum_sum[l:mid + 1]:
                while i <= r and cum_sum[i] - left < lower:
                    i += 1
                
                while j <= r and cum_sum[j] - left <= upper:
                    j += 1
                
                cnt += j - i
            
            cum_sum[l:r + 1] = sorted(cum_sum[l:r + 1])

            return cnt
        
        return mergesort(0, len(cum_sum) - 1)
