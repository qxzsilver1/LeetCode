class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        
        def swap(i, pivot_idx):
            tmp = nums[i]
            nums[i] = nums[pivot_idx]
            nums[pivot_idx] = tmp
            return
        
        def partition(l, r):
            pivot_val = nums[r]
            i = l

            for j in range(l, r + 1):
                if nums[j] < pivot_val:
                    swap(i, j)
                    i += 1
            
            swap(r, i)
            return i
        
        def select(l, r, k):
            if l == r:
                return nums[l]
            
            pivot_idx = partition(l, r)

            if k == pivot_idx:
                return nums[k]
            elif k < pivot_idx:
                return select(l, pivot_idx - 1, k)
            else:
                return select(pivot_idx + 1, r, k)
        
        median = select(0, n - 1, n // 2)

        for num in nums:
            res += abs(median - num)
        
        return res
