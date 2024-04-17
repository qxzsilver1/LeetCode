class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next

        self.head.next = node

        if not node.next:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        while curr and index > 0:
            index -= 1
            curr = curr.next
        
        if curr and index == 0:
            node = ListNode(val)
            
            tmp = curr.next
            node.next = tmp
            curr.next = node

            if not node.next:
                self.tail = node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head

        while curr and index > 0:
            index -= 1
            curr = curr.next
        
        if curr and curr.next and index == 0:
            if curr.next == self.tail:
                self.tail = curr
            
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
