class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        score = nums[0]

        q = deque()
        q.append((0, score))

        for i in range(1, n):
            while q and q[0][0] < i - k:
                q.popleft()
            
            score = q[0][1] + nums[i]

            while q and score >= q[-1][1]:
                q.pop()
            
            q.append((i, score))
        
        return score
