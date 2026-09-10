# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if length == 1:
            return head.next
        
        removeNextNode = length - n
        if removeNextNode == 0:
            return head.next

        curr = head
        i = 0
        while curr:
            print(curr.val)
            i += 1
            if i == removeNextNode:
                curr.next = curr.next.next
                return head
            curr = curr.next


