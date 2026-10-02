class Node:
    def __init__(self, key, value):
        self.key, self.value = key,value
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.cache = {}
        self.LRU, self.mostRecent = Node(0,0), Node(0,0)
        self.LRU.next, self.mostRecent.prev = self.mostRecent, self.LRU
        
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:  
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if len(self.cache) > self.maxCapacity:
            removeNode = self.LRU.next
            self.remove(removeNode)
            del self.cache[removeNode.key]
    
    def add(self, node):
        prev = self.mostRecent.prev
        prev.next = node
        node.prev = prev
        node.next = self.mostRecent
        self.mostRecent.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev =  node.prev

