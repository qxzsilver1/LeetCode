class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        cnt = 0

        for c in zip(*picture):
            if c.count('B') != target:
                continue
            
            first_row = picture[c.index('B')]

            if first_row.count('B') != target:
                continue
            
            if picture.count(first_row) != target:
                continue
            
            cnt += 1
        
        return cnt * target
