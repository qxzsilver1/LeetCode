class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        self.val = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.end_of_word = True
        curr.val = word
        

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        
        return curr.end_of_word
        

    def bfs(self):
        q = deque([self.root])
        res = ''

        while q:
            curr = q.popleft()

            for child in curr.children.values():
                if child.end_of_word:
                    q.append(child)

                    if len(child.val) > len(res):
                        res = child.val
        
        return res

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        return trie.bfs()
