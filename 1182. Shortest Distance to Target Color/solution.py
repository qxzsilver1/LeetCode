class Solution:
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        n = len(colors)

        dist = [[n] * 4 for _ in colors]

        for color in range(1, 4):
            last = -n

            for i in range(n):
                if colors[i] == color:
                    last = i
                dist[i][color] = i - last
            last = 2 * n

            for i in range(n - 1, -1, -1):
                if colors[i] == color:
                    last = i
                dist[i][color] = min(dist[i][color], last - i)
        
        return [dist[i][c] if dist[i][c] < n else - 1 for i, c in queries]
