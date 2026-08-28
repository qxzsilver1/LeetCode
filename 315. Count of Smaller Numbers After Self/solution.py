class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(idx, val, tree, size):
            idx += size

            tree[idx] += val

            while idx > 1:
                idx //= 2
                tree[idx] = tree[2 * idx] + tree[2* idx + 1]
        
        def query(left, right, tree, size):
            res = 0

            left += size
            right += size

            while left < right:
                if left % 2:
                    res += tree[left]
                    left += 1
                
                left //= 2

                if right % 2:
                    right -= 1
                    res += tree[right]
                
                right //= 2
            
            return res
        
        offset = 10 ** 4 # lowest possible negative value in input offset to make values non-negative
        size = 2 * 10 ** 4 + 1 # total possible range of values of input

        tree = [0] * (2 * size)
        res = []

        for num in reversed(nums):
            smaller_cnt = query(0, num + offset, tree, size)
            res.append(smaller_cnt)
            update(num + offset, 1, tree, size)
        
        return res[::-1]
