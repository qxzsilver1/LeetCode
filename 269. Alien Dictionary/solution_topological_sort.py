class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = { c: set() for w in words for c in w }
        indegrees = {c: 0 for c in adj_list}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ''
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_list[w1[j]]:
                        adj_list[w1[j]].add(w2[j])
                        indegrees[w2[j]] += 1
                    break
        
        q = deque([c for c in indegrees if indegrees[c] == 0])

        res = []

        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj_list[c]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indegrees):
            return ''
        
        return ''.join(res)
