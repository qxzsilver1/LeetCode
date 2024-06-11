class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def increase(self, num):
        curr = self.root

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            
            curr = curr.children[bit]
    
    def findMax(self, num):
        curr = self.root
        res = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if (1 - bit) in curr.children:
                curr = curr.children[1 - bit]
                res |= (1 << i)
            else:
                curr = curr.children[bit]
        
        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()

        for n in nums:
            trie.increase(n)
        
        res = 0

        for n in nums:
            res = max(res, trie.findMax(n))

        return res
