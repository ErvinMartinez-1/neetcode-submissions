class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU, self.mostRecent = Node(0, 0), Node(0, 0)
        self.LRU.next, self.mostRecent.prev = self.mostRecent, self.LRU
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:  
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        
        if len(self.cache) > self.capacity:
            nodeToRemove = self.LRU.next
            self.remove(nodeToRemove)
            del self.cache[nodeToRemove.key]
    
    def add(self, node):
        prev = self.mostRecent.prev
        prev.next = node
        node.prev = prev
        node.next = self.mostRecent
        self.mostRecent.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


