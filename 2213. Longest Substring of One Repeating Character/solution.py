class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        
        prefix_len = [0] * (4*n)
        suffix_len = [0] * (4*n)

        max_len = [0] * (4*n)

        left_char = [''] * (4*n)
        right_char = [''] * (4*n)

        def build(u, l, r):
            if l == r:
                prefix_len[u] = 1
                suffix_len[u] = 1
                max_len[u] = 1

                left_char[u] = s[l]
                right_char[u] = s[l]

                return
            
            m = (l + r) >> 1

            build(u << 1, l, m)
            build(u << 1 | 1, m + 1, r)

            pushUp(u, l, r)
        
        def pushUp(u, l, r):
            m = (l + r) >> 1
            left_len = m - l + 1
            right_len = r - m

            left, right = u << 1, u << 1 | 1

            left_char[u] = left_char[left]
            right_char[u] = right_char[right]

            prefix_len[u] = prefix_len[left]

            if prefix_len[left] == left_len and right_char[left] == left_char[right]:
                prefix_len[u] = prefix_len[left] + prefix_len[right]
            
            suffix_len[u] = suffix_len[right]

            if suffix_len[right] == right_len and right_char[left] == left_char[right]:
                suffix_len[u] = suffix_len[right] + suffix_len[left]
            
            max_len[u] = max(max_len[left], max_len[right])

            if right_char[left] == left_char[right]:
                max_len[u] = max(max_len[u], suffix_len[left] + prefix_len[right])
            
        def update(u, l, r, pos, ch):
            if l == r:
                left_char[u] = ch
                right_char[u] = ch
                return
            
            m = (l + r ) >> 1

            if pos <= m:
                update(u << 1, l, m, pos, ch)
            else:
                update(u << 1 | 1, m + 1, r, pos, ch)
            
            pushUp(u, l, r)
        
        build(1, 0, n-1)

        k = len(queryIndices)

        res = []

        for i in range(k):
            update(1, 0, n-1, queryIndices[i], queryCharacters[i])
            res.append(max_len[1])
        
        return res
