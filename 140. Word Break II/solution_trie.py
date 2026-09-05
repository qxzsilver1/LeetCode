class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        def backtrack(i, path):
            if i == len(s):
                res.append(" ".join(path))
                return

            node = trie.root
            word = []
            for i in range(i, len(s)):
                char = s[i]
                if char not in node.children:
                    break

                word.append(char)
                node = node.children[char]

                if node.isWord:
                    path.append("".join(word))
                    backtrack(i + 1, path)
                    path.pop()

        res = []
        backtrack(0, [])
        return res
