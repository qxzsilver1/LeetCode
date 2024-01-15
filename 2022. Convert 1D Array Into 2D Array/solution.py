class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        output = []
        
        for i in range(m):
            output.append(original[i*n:i*n + n])
        
        return output
