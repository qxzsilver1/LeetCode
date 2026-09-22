class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort()

        dp = [[-1] * 3 for _ in range(len(events))]

        def findEvents(idx, cnt):
            if cnt == 2 or idx >= len(events):
                return 0
            
            if dp[idx][cnt] == -1:
                end = events[idx][1]

                l, r = idx + 1, len(events) - 1

                while l < r:
                    m = l + (r - l) // 2

                    if events[m][0] > end:
                        r = m
                    else:
                        l = m + 1
                
                included = events[idx][2] + (findEvents(l, cnt + 1) if l < len(events) and events[l][0] > end else 0)
                
                excluded = findEvents(idx + 1, cnt)

                dp[idx][cnt] = max(included, excluded)
            
            return dp[idx][cnt]
        
        return findEvents(0, 0)
