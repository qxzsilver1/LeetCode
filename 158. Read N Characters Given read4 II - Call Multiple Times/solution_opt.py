# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.pending = [''] * 4
        self.index = self.size = 0
    
    def read(self, buf: List[str], n: int) -> int:
        written = 0
        while written < n:
            if self.index == self.size:
                self.size = read4(self.pending)
                self.index = 0
                if self.size == 0:
                    break
            buf[written] = self.pending[self.index]
            written += 1
            self.index += 1
        return written
