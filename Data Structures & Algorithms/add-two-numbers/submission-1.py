# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stck1, stck2 = [], []

        head1 = l1
        while head1:
            stck1.append(head1.val)
            head1 = head1.next
        
        val1 = ""
        while stck1:
            val1 += str(stck1.pop())
        
        head2 = l2
        while head2:
            stck2.append(head2.val)
            head2 = head2.next
        
        val2 = ""
        while stck2:
            val2 += str(stck2.pop())

        result = str(int(val1) + int(val2))
        dummy = head = ListNode()
        for i in range(len(result) - 1, -1, -1):
            temp = ListNode(int(result[i]))
            head.next = temp
            head = head.next

        return dummy.next
        
        
    