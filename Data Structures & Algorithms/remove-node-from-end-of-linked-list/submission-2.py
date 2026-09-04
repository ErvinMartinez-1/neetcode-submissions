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
        
        remove = length - n + 1
        print(remove)
        if remove == 1:
            return head.next
        count = 1
        curr = head
        while curr:
            if count == remove - 1:
                curr.next = curr.next.next
                return head
            curr = curr.next
            count += 1