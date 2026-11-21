class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        head = [-1] * n
        nxt = [-1] * n
        
        for i in range(n - 1, 0, -1):
            nxt[i] = head[parent[i]]
            head[parent[i]] = i

        c = [ord(ch) - 97 for ch in s]
        last = [-1] * 26
        prev = [-1] * n
        order = [0]
        stack = [0]
        last[c[0]] = 0

        while stack:
            u = stack[-1]
            v = head[u]
            if v != -1:
                head[u] = nxt[v]
                prev[v] = last[c[v]]
                last[c[v]] = v
                order.append(v)
                stack.append(v)
            else:
                last[c[u]] = prev[u]
                stack.pop()

        ans = [1] * n
        
        for k in range(n - 1, 0, -1):
            x = order[k]
            p = prev[x] if prev[x] != -1 else parent[x]
            ans[p] += ans[x]
        return ans
