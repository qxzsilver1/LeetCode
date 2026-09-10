class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = list()

        for i in range(1024):
            h = i >> 6
            m = i & 0x3F

            if h < 12 and m < 60 and bin(i).count('1') == turnedOn:
                res.append(f'{h}:{m:02d}')
            
        return res
