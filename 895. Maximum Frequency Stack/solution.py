class FreqStack:

    def __init__(self):
        self.cnt_list = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.cnt_list[val] = 1 + self.cnt_list.get(val, 0)

        if self.cnt_list[val] > self.max_count:
            self.max_count = self.cnt_list[val]
            self.stacks[self.cnt_list[val]] = []
        
        self.stacks[self.cnt_list[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.cnt_list[res] -= 1

        if not self.stacks[self.max_count]:
            self.max_count -= 1
        
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
