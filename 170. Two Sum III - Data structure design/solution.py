class TwoSum:

    def __init__(self):
        self.num_freq = {}

    def add(self, number: int) -> None:
        if number in self.num_freq:
            self.num_freq[number] += 1
        else:
            self.num_freq[number] = 1
        

    def find(self, value: int) -> bool:
        for num in self.num_freq.keys():
            complement = value - num

            if num != complement:
                if complement in self.num_freq:
                    return True
            elif self.num_freq[num] > 1:
                return True
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
