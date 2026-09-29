class FirstUnique:

    def __init__(self, nums: list[int]):
        self._queue = OrderedDict()
        self._is_unique = {}

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:  
        if self._queue:
            return next(iter(self._queue))
        
        return -1

    def add(self, value: int) -> None:
        if value not in self._is_unique:
            self._is_unique[value] = True
            self._queue[value] = None
        elif self._is_unique[value]:
            self._is_unique[value] = False
            self._queue.pop(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
