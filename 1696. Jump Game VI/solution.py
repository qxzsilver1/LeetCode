class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        scores = [0] * n

        scores[0] = nums[0]

        q = deque()
        q.append(0)

        for i in range(1, n):
            while q and q[0] < i - k:
                q.popleft()
            
            scores[i] = scores[q[0]] + nums[i]

            while q and scores[i] >= scores[q[-1]]:
                q.pop()
            q.append(i)
        
        return scores[-1]
