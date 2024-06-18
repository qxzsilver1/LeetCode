class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.idx = -1

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()

        for i in range(len(folder)):
            curr = self.root

            for c in folder[i]:
                curr = curr.children[c]
            
            curr.idx = i
        
        q = deque([self.root])
        res = []

        while q:
            node = q.popleft()

            if node.idx >= 0:
                res.append(folder[node.idx])
            
            for c in node.children.keys():
                if '/' != c or node.idx < 0:
                    q.append(node.children.get(c))
        
        return res
