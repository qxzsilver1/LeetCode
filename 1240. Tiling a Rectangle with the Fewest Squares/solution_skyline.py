class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:

        @lru_cache(None)
        def dp(skyline):
            l = 0
            min_height = float('inf')

            for i, h in enumerate(skyline):
                if h < min_height:
                    min_height = h
                    l = i

            if min_height == n:
                return 0
            
            new_skyline = list(skyline)
            res = float('inf')

            for r in range(l, m):
                if new_skyline[r] == min_height:
                    tile_width = r - l + 1

                    if tile_width + min_height <= n:
                        new_skyline[l:r+1] = [tile_width + min_height] * tile_width
                        res = min(res, dp(tuple(new_skyline)) + 1)             
                else:
                    break
            
            return res
        
        return dp(tuple([0]*m))
