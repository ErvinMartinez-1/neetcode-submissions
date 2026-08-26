# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        nodePlace = length - n
        if nodePlace == 0:
            return head.next

        for i in range(length - 1):
            if (i + 1) == nodePlace:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head