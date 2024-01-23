class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        source_color = image[sr][sc]
        if source_color == newColor:
            return image
        
        def dfs(image, sr, sc, newColor, sourceColor):
            if sr < 0 or sr >= m:
                return
            
            if sc < 0 or sc >= n:
                return
            
            if image[sr][sc] != sourceColor:
                return
            
            image[sr][sc] = newColor

            dfs(image, sr+1, sc, newColor, sourceColor)
            dfs(image, sr-1, sc, newColor, sourceColor)
            dfs(image, sr, sc+1, newColor, sourceColor)
            dfs(image, sr, sc-1, newColor, sourceColor)
        
        dfs(image, sr, sc, newColor, source_color)

        return image
        
