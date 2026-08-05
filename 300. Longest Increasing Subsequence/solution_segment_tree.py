from bisect import bisect_left

class SegmentTree:
    def __init__(self, N):
        self.n = N

        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        
        self.tree = [0] * (2 * self.n)
    
    def update(self, i, val):
        self.tree[self.n + i] = val
        j = (self.n + i) >> 1

        while j >= 1:
            self.tree[j] = max(self.tree[j << 1], self.tree[j << 1 | 1])
            j >>= 1
    
    def query(self, l, r):
        if l > r:
            return 0
        
        res = float('-inf')

        l += self.n
        r += self.n + 1

        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            
            l >>= 1
            r >>= 1
        
        return res

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def compressArray(arr):
            sorted_arr = sorted(set(arr))
            order = []

            for num in arr:
                order.append(bisect_left(sorted_arr, num))
            
            return order
        
        nums = compressArray(nums)

        n = len(nums)
        segment_tree = SegmentTree(n)

        longest_incr_subseq = 0

        for num in nums:
            curr_longest_incr_subseq = segment_tree.query(0, num-1) + 1
            segment_tree.update(num, curr_longest_incr_subseq)
            longest_incr_subseq = max(longest_incr_subseq, curr_longest_incr_subseq)
        
        return longest_incr_subseq
