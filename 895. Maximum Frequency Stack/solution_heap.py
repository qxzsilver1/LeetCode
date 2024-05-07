class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.heap = []
        self.idx = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.idx += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.idx, val))

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
