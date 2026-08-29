# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        
        def printLinkedListInReverseRecursively(head, size):
            if size > 0 and head:
                printLinkedListInReverseRecursively(head.getNext(), size - 1)
                head.printValue()
        
        def getLinkedListSize(head):
            size = 0

            while head:
                size += 1
                head = head.getNext()
            
            return size
        
        linked_list_size = getLinkedListSize(head)
        block_size = math.ceil(math.sqrt(linked_list_size))

        blocks = []

        curr = head

        for i in range(linked_list_size):
            if i % block_size == 0:
                blocks.append(curr)
            curr = curr.getNext()
        
        while blocks:
            printLinkedListInReverseRecursively(blocks.pop(), block_size)
