class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()

        for sentence, cnt in zip(sentences, times):
            self.addToTrie(sentence, cnt)
        
        self.curr_sentence = []
        self.curr_node = self.root
        self.dead = TrieNode()     

    def input(self, c: str) -> List[str]:
        if c == '#':
            curr_sentence = ''.join(self.curr_sentence)
            self.addToTrie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.curr_sentence.append(c)

        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        
        items = [(val, key) for key, val in self.curr_node.sentences.items()]
        res = heapq.nsmallest(3, items)

        return [item[1] for item in res]
    
    def addToTrie(self, sentence: str, count: int):
        node = self.root

        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]
            node.sentences[sentence]  -= count

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
