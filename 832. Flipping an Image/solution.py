class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = [x ^ 1 for x in image[i]]
            image[i] = image[i][::-1]
        
        return image
