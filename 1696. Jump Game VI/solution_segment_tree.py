class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        def update(index, value, tree, n):
            index += n
            tree[index] = value
            
            while index > 1:
                index >>= 1
                tree[index] = max(tree[index << 1], tree[(index << 1)+1])

        def query(left, right, tree, n):
            result = -inf
            left += n
            right += n
            
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                left >>= 1
                
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                right >>= 1
            return result

        n = len(nums)
        tree = [0]*(2*n)
        update(0, nums[0], tree, n)
        
        for i in range(1, n):
            maxi = query(max(0, i-k), i, tree, n)
            update(i, maxi+nums[i], tree, n)
        
        return tree[-1]
