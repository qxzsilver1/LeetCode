class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        res = 0
        end, farthest = 0, 0

        clips.sort()

        i = 0
        while farthest < time:
            while i < len(clips) and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])

                i += 1
            
            if end == farthest:
                return -1
            
            res += 1
            end = farthest
        
        return res
