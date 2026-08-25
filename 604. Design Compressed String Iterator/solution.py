import re

class StringIterator:

    def __init__(self, compressedString: str):
        self.ptr = 0
        self.nums = list(map(int, re.findall(r'\d+', compressedString)))
        self.chars = re.findall(r'[a-zA-Z]', compressedString)

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        self.nums[self.ptr] -= 1

        res = self.chars[self.ptr]

        if self.nums[self.ptr] == 0:
            self.ptr += 1
        
        return res

    def hasNext(self) -> bool:
        return self.ptr != len(self.chars)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
