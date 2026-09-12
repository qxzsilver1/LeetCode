class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = [(end, start, weight, i) for i, (start, end, weight) in enumerate(intervals)]

        arr.sort(key= lambda x: x[0])

        dp = [[0] * 5 for _ in range(n + 1)]
        indices = [[[] for _ in range(5)] for _ in range(n + 1)]

        for i in range(n):
            r, l, weight, idx = arr[i]

            k = bisect_left(arr, (l, ), hi= i)

            for j in range(1, 5):
                s1 = dp[i][j]
                s2 = dp[k][j - 1] + weight

                if s1 > s2:
                    dp[i + 1][j] = dp[i][j]
                    indices[i + 1][j] = indices[i][j].copy()
                    continue
                
                next_idx = indices[k][j - 1].copy()
                next_idx.append(idx)
                next_idx.sort()

                if s1 == s2 and indices[i][j] < next_idx:
                    next_idx = indices[i][j].copy()
                
                dp[i + 1][j] = s2
                indices[i + 1][j] = next_idx
        
        return indices[n][4]
