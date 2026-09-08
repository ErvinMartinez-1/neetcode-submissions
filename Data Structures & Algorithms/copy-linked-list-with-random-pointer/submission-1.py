"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        curr = head
        oldToNew = defaultdict()

        while curr:
            new = Node(x=curr.val)
            oldToNew[curr] = new
            curr = curr.next
        
        curr = head
        while curr:
            node = oldToNew[curr]
            node.next = oldToNew[curr.next] if curr.next else None
            node.random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
        return oldToNew[head]

