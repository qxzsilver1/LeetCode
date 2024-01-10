class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum_arr = []
        curr_sum = 0

        for n in nums:
            curr_sum += n
            self.prefix_sum_arr.append(curr_sum)

    def update(self, index: int, val: int) -> None:
        if index == 0:
            val_delta = val - self.prefix_sum_arr[index]
            for i in range(len(self.prefix_sum_arr)):
                self.prefix_sum_arr[i] += val_delta
        else:
            val_delta = val - (self.prefix_sum_arr[index] - self.prefix_sum_arr[index-1])
            for i in range(index, len(self.prefix_sum_arr)):
                self.prefix_sum_arr[i] += val_delta

    def sumRange(self, left: int, right: int) -> int:
        r_sum = self.prefix_sum_arr[right]
        l_sum = self.prefix_sum_arr[left - 1] if left > 0 else 0

        return r_sum - l_sum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
