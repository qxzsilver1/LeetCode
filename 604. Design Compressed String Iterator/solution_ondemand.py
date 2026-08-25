import re

class StringIterator:

    def __init__(self, compressedString: str):
        self.res = compressedString
        self.ptr = 0
        self.num = 0
        self.ch = ' '

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        if self.num == 0:
            self.ch = self.res[self.ptr]
            self.ptr += 1

            while self.ptr < len(self.res) and self.res[self.ptr].isdigit():
                self.num = 10 * self.num + int(self.res[self.ptr])
                self.ptr += 1
        
        self.num -= 1
        
        return self.ch

    def hasNext(self) -> bool:
        return self.ptr != len(self.res) or self.num != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
