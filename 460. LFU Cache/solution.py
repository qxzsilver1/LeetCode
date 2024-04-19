class ListNode:
    def __init__(self, val, prev= None, next= None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}
    
    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node
    
    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            nxt, prev = node.next, node.prev
            nxt.prev = prev
            prev.next = nxt
            self.map.pop(val, None)
    
    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0
        self.val_map = {} # maps the key -> val
        self.count_map = defaultdict(int) # maps the key -> count
        self.list_map = defaultdict(LinkedList) # maps the keycount -> linked list
    
    def counter(self, key):
        cnt = self.count_map[key]
        self.count_map[key] += 1
        self.list_map[cnt].pop(key)
        self.list_map[cnt + 1].pushRight(key)

        if cnt == self.lfu_count and self.list_map[cnt].length() == 0:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.val_map:
            return -1
        
        self.counter(key)
        return self.val_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key not in self.val_map and len(self.val_map) == self.capacity:
            res = self.list_map[self.lfu_count].popLeft()
            self.val_map.pop(res)
            self.count_map.pop(res)

        self.val_map[key] = value
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.count_map[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
