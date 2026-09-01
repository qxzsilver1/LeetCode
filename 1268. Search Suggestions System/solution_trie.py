class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()

            node = node.children[i]

        node.isEnd = True

    def prefSearch(self, pref):
        node = self.root

        for i in pref:
            if i not in node.children:
                return []

            node = node.children[i]

        res = []

        def dfs(node, path):
            if len(res) == 3:
                return

            if node.isEnd:
                res.append(path)

            for i in sorted(node.children):
                dfs(node.children[i], path + i)

                if len(res) == 3:
                    return

        dfs(node, pref)

        return res


class Solution:
    def suggestedProducts(
        self,
        products: List[str],
        searchWord: str
    ) -> List[List[str]]:

        t = Trie()

        for i in products:
            t.insert(i)

        op = []
        pre = ''

        for i in searchWord:
            pre += i
            op.append(t.prefSearch(pre))

        return op
