class MovingAverage:

    def __init__(self, size: int):
        self.capacity = size
        self.curr_size = 0
        self.curr_avg = 0
        self.window_array = [0] * size

        self.curr_pos = 0

    def next(self, val: int) -> float:
        if self.capacity == self.curr_size:
            self.curr_avg = (self.curr_avg * self.curr_size - self.window_array[self.curr_pos] + val) / (self.curr_size)
            self.window_array[self.curr_pos] = val
            self.curr_pos += 1
            self.curr_pos %= self.capacity
        else:
            self.curr_avg = (self.curr_avg * self.curr_size + val) / (self.curr_size + 1)
            self.curr_size += 1
            self.window_array[self.curr_pos] = val
            self.curr_pos += 1
            self.curr_pos %= self.capacity
        
        return self.curr_avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
