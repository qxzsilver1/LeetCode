class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        tree = SortedDict()

        l = 0
        res = 0

        for r, x in enumerate(nums):
            tree[x] = tree.get(x, 0) + 1

            while tree.peekitem(-1)[0] - tree.peekitem(0)[0] > limit:
                y = nums[l]
                tree[y] -= 1
                
                if tree[y] == 0:
                    del tree[y]
                
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
