class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [float('-inf')] * (len(nums) - k + 1)
        
        l, r = 0, 0
        q = deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove left value if out of bounds
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res[l] = nums[q[0]]
                l += 1
            
            r += 1
        
        return res
