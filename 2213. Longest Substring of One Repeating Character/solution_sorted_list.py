class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        
        segments = SortedList()
        lengths = SortedList()

        i = 0

        while i < n:
            j = i

            while j < n and s[j] == s[i]:
                j += 1
            
            segments.add((i, j-1))
            lengths.add(j-i)
            i = j
        
        k = len(queryIndices)

        res = []

        for q in range(k):
            pos = queryIndices[q]
            ch = queryCharacters[q]

            if s[pos] != ch:
                idx = segments.bisect_right((pos, n)) - 1
                l, r = segments[idx]
                segments.pop(idx)
                lengths.remove(r - l + 1)

                if l <= pos - 1:
                    segments.add((l, pos - 1))
                    lengths.add(pos - l)
                
                if pos + 1 <= r:
                    segments.add((pos + 1, r))
                    lengths.add(r - pos)
                
                new_l, new_r = pos, pos

                if pos + 1 < n and s[pos + 1] == ch:
                    idx2 = segments.bisect_left((pos + 1, -1))

                    if idx2 < len(segments) and segments[idx2][0] == pos + 1:
                        right_l, right_r = segments[idx2]
                        lengths.remove(right_r - right_l + 1)
                        new_r = right_r
                        segments.pop(idx2)
                
                if pos > 0 and s[pos - 1] == ch:
                    idx3 = segments.bisect_right((pos - 1, n)) - 1

                    if idx3 >= 0 and segments[idx3][1] == pos - 1:
                        left_l, left_r = segments[idx3]
                        lengths.remove(left_r - left_l + 1)
                        new_l = left_l
                        segments.pop(idx3)
                
                segments.add((new_l, new_r))
                lengths.add(new_r - new_l + 1)
                s[pos] = ch
            
            res.append(lengths[-1])
        
        return res
