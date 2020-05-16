# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        oddPointer,evenPointer, even = head, head.next, head.next
        while evenPointer != None and evenPointer.next != None:
            oddPointer.next = oddPointer.next.next
            oddPointer = oddPointer.next
            evenPointer.next = evenPointer.next.next
            evenPointer = evenPointer.next
            
        oddPointer.next = even
        
        return head
        
