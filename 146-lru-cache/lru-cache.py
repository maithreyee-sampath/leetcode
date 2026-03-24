class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {} #store the map of key inserted in our doubly ll
        #append at most and remove at least
        self.most = Node(0,0)
        self.least = Node(0,0)

        self.least.next, self.most.prev = self.most,self.least
    
    def insert(self,node):
        p = self.most.prev
        
        node.next = self.most
        p.next = node
        node.prev = p
        self.most.prev = node


    def remove(self,node):
        p,n = node.prev,node.next
        p.next,n.prev = n,p
        return

    def get(self, key: int) -> int:
        
        
        #get the value and it should be the most recent one accessed
        if key not in self.map:
            return -1
        
        # remove it form our map and reinsert it at the rightmost pos
        node = self.map[key]
        self.remove(node)
        self.insert(node)
    
        return node.val
            

        #most recently should point to this node 

    def put(self, key: int, value: int) -> None:
        #insert node at given key

        #if key already exists we remove it
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key,value) #store it in our hashmap
        self.insert(self.map[key]) #also insert it into our dll

        if len(self.map) > self.cap:
            #remove lru
            lru = self.least.next
            self.remove(lru)
            del self.map[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)