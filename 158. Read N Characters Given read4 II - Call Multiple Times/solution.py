# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = []
    
    def read(self, buf: List[str], n: int) -> int:
        buffer_cnt = 0

        while len(self.buffer) < n:
            buf4 = ['' for i in range(4)]
            cnt = read4(buf4)

            if cnt > 0:
                for i in range(cnt):
                    self.buffer.append(buf4[i])
            else:
                break
        
        for i in range(n):
            if len(self.buffer) == 0:
                break
            
            buf[buffer_cnt] = self.buffer.pop(0)
            buffer_cnt += 1
        
        return buffer_cnt
