class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(10000)]
    
    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
    
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)].next

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
    
        return -1

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
