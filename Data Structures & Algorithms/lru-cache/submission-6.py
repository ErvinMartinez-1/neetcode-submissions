class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU, self.mostRecent = Node(0,0), Node(0,0)
        self.LRU.next, self.mostRecent.prev = self.mostRecent, self.LRU
    
    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev, prev.next = prev, next
    
    def add(self, node):
        prev = self.mostRecent.prev
        prev.next = node
        node.prev = prev
        node.next = self.mostRecent
        self.mostRecent.prev = node
        
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
            node = self.LRU.next
            self.remove(node)
            del self.cache[node.key]

