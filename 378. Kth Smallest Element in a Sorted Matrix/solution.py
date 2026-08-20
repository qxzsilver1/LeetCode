class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        l, r = matrix[0][0], matrix[n-1][n-1]

        def countLessEqual(matrix, mid, smaller, larger):
            cnt = 0
            n = len(matrix)

            r, c = n-1, 0

            while r >= 0 and c < n:
                if matrix[r][c] > mid:
                    larger = min(larger, matrix[r][c])
                    r -= 1
                else:
                    smaller = max(smaller, matrix[r][c])
                    cnt += r + 1
                    c += 1
            
            return cnt, smaller, larger

        while l < r:
            m = l + (r - l) // 2
            smaller, larger = matrix[0][0], matrix[n-1][n-1]

            cnt, smaller, larger = countLessEqual(matrix, m, smaller, larger)

            if cnt == k:
                return smaller
            
            if cnt < k:
                l = larger
            else:
                r = smaller
        
        return l
