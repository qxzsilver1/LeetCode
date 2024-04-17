class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and curr != self.right and index == 0:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        nxt, prev = self.left.next, self.left

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        nxt, prev = self.right, self.right.prev

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            index -= 1
            curr = curr.next
        
        if curr and index == 0:
            node = ListNode(val)
            nxt, prev = curr, curr.prev

            prev.next = node
            nxt.prev = node
            node.next = nxt
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            index -= 1
            curr = curr.next
        
        if curr and curr != self.right and index == 0:
            nxt, prev = curr.next, curr.prev

            prev.next = nxt
            nxt.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
