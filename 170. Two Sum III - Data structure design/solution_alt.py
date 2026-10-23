class TwoSum:

    def __init__(self):
        self.counts = {}
    
    def add(self, number: int) -> None:
        self.counts[number] = self.counts.get(number, 0) + 1
    
    def find(self, value: int) -> bool:
        return any(value-x in self.counts and (value-x != x or c > 1) for x,c in self.counts.items())


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
