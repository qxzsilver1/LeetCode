class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        counts = {}
        cols = [0] * len(picture[0])
        
        for row in picture:
            key = ''.join(row)
            counts[key] = counts.get(key,0) + 1
            
            for j, v in enumerate(row):
                cols[j] += v == 'B'
        
        return sum(target for row,count in counts.items() if count == target and row.count('B') == target for j, v in enumerate(row) if v == 'B' and cols[j] == target)
