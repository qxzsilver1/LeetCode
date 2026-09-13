class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        import numpy as np
        img1 = np.array(img1)
        img2 = np.array(img2)

        dim = len(img1)
        # extend the matrix to a wider range for the later kernel extraction.
        img2_padded = np.pad(img2, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = img2_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(img1 * kernel)
                max_overlaps = max(max_overlaps, int(non_zeros))

        return max_overlaps
