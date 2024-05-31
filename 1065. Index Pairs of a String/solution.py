class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    @staticmethod
    def build_trie(words_list):
        root = TrieNode()

        for word in words_list:
            node = root

            for c in word:
                node.children.setdefault(c, TrieNode())
                node = node.children[c]
            
            node.end_of_word = True
        
        return root

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        trie = Trie.build_trie(words)

        for l in range(len(text)):
            node = trie

            for r in range(l, len(text)):
                if text[r] not in node.children:
                    break
                
                node = node.children[text[r]]

                if node.end_of_word:
                    res.append([l, r])
        
        return res
