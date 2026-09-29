class FirstUnique:

    def __init__(self, nums: list[int]):
        self._queue = deque(nums)
        self._is_unique = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self._queue and not self._is_unique[self._queue[0]]:
            self._queue.popleft()
        
        if self._queue:
            return self._queue[0]
        
        return -1

    def add(self, value: int) -> None:
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue.append(value)
        else:
            self._is_unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
