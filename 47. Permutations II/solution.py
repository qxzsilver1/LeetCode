class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums_dict = Counter(nums)

        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for n in nums_dict:
                if nums_dict[n] > 0:
                    perm.append(n)
                    nums_dict[n] -= 1

                    dfs()

                    nums_dict[n] += 1
                    perm.pop()
        
        dfs()
        
        return res
