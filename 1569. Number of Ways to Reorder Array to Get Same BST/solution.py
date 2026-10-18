class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7

        def dfs(arr):
            m = len(arr)

            if m < 3:
                return 1
            
            left_nodes = [a for a in arr if a < arr[0]]
            right_nodes = [a for a in arr if a > arr[0]]

            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % MOD
        
        return (dfs(nums) - 1) % MOD
