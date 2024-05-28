class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate_matrix():
            nonlocal mat

            l, r = 0, len(mat[0]) - 1

            while l < r:
                for i in range(r - l):
                    top, bottom = l, r

                    top_left = mat[top][l + i]
                    mat[top][l + i] = mat[bottom - i][l]
                    mat[bottom - i][l] = mat[bottom][r - i]
                    mat[bottom][r - i] = mat[top + i][r]
                    mat[top + i][r] = top_left
                
                r -= 1
                l += 1
        
        for _ in range(4):
            if mat == target:
                return True
            
            rotate_matrix()
        
        return False
