class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.binary_indexed_tree = [0] + nums[:]

        for i in range(1, self.n + 1):
            j = i + (i & -i)
            if j <= self.n:
                self.binary_indexed_tree[j] += self.binary_indexed_tree[i]

    def update(self, index: int, val: int) -> None:
        val_delta = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= self.n:
            self.binary_indexed_tree[index] += val_delta
            index += (index & -index)

    def sumRange(self, left: int, right: int) -> int:
        return self.getPrefix(right) - self.getPrefix(left-1)
    
    def getPrefix(self, i: int) -> int:
        i += 1
        res = 0

        while i > 0:
            res += self.binary_indexed_tree[i]
            i -= (i & -i)

        return res



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
