class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(idx, val, tree, size):
            idx += 1

            while idx < size:
                tree[idx] += val
                idx += idx & (- idx)
        
        def query(idx, tree):
            res = 0

            while idx >= 1:
                res += tree[idx]
                idx -= idx & (- idx)
            
            return res
        
        offset = 10 ** 4 # lowest possible negative value in input offset to make values non-negative
        size = 2 * 10 ** 4 + 2 # total possible range of values of input

        tree = [0] * size
        res = []

        for num in reversed(nums):
            smaller_cnt = query(num + offset, tree)
            res.append(smaller_cnt)
            update(num + offset, 1, tree, size)
        
        return res[::-1]
