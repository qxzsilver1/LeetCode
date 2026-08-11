class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        visited = [False] * n

        digit_sum = lambda x: (sum(map(int, str(nums[x]))), nums[x])

        perm = sorted(range(n), key = digit_sum)

        for i in range(n):
            if visited[i]:
                continue
            
            res -= 1
            curr = i

            while not visited[curr]:
                visited[curr] = True
                curr = perm[curr]
        
        return res
