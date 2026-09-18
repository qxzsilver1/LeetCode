class Segment:
    def __init__(self, left= -1, right= -1):
        self.left = left
        self.right = right
    
    def __lt__(self, rhs):
        return self.left > rhs.left if self.right == rhs.right else self.right < rhs.right

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        segs = [Segment() for _ in range(26)]

        for i in range(len(s)):
            char_idx  = ord(s[i]) - ord('a')

            if segs[char_idx].left == -1:
                segs[char_idx].left = segs[char_idx].right = i
            else:
                segs[char_idx].right = i
        
        for i in range(26):
            if segs[i].left != -1:
                j = segs[i].left

                while j <= segs[i].right:
                    char_idx = ord(s[j]) - ord('a')

                    if segs[i].left <= segs[char_idx].left and segs[char_idx].right <= segs[i].right:
                        pass
                    else:
                        segs[i].left = min(segs[i].left, segs[char_idx].left)
                        segs[i].right = max(segs[i].right, segs[char_idx].right)
                        j = segs[i].left
                    j += 1
        
        segs.sort()

        res = []
        end = -1

        for seg in segs:
            l, r = seg.left, seg.right

            if l == -1:
                continue
            
            if end == -1 or l > end:
                end = r
                res.append(s[l:r + 1])
        
        return res
