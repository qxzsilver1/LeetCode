class SegmentTree:
    
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def query(self, left, right):
        left += self.n
        right += self.n + 1

        res = 0

        while left < right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1
            
            if right % 2 == 1:
                right -= 1
                res += self.tree[right]
            
            left //= 2
            right //= 2
        
        return res

class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = SegmentTree(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.query(left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
