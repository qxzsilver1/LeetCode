# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def helper(start, end):
            if start is None or start == end:
                return
            
            if start.getNext() == end:
                start.printValue()
                return
            
            slow, fast = start, start

            while fast != end and fast.getNext() != end:
                slow = slow.getNext()
                fast = fast.getNext().getNext()
            
            helper(slow, end)
            helper(start, slow)
        
        helper(head, None)
