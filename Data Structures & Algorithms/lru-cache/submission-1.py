class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:
    # 1. init take a capacity to create a cache
    # 2. get is quick look up O(1), update the recent 
    # 3. put should 
    #     check exist
    #     1. True, update 
    #     2. False, create a new key - > if cache is full, remove least recently used key
    # O(1)
    # because we want O1 for both get and put, we have limited options
    # 1. quick look up. hashmap style 
    #     update into the recent order, this one is tricky since we dont want any sorting logic here(logn), then linklist should be a good choice
    # 2. quick insert and delete, hashmap is good
    # so for the hashmap, we use key as key, value 
    # for the ll, I start with only one head, then found that there is no way we can track both side
    # why we need this?
    # because we want to build a LL can represent the time series of operations
    # if we only have one head, then for example we always refresh the most recent as the next node from head
    # when the cap is full, we wnat to remove, we are removing the tail position, so we need a pointer at there no matter what for O1
    # so I guess we might need another boundary node as tail, but I will first use tail as only a pointer to see if this is work
    # for the LL and hashmap design, there is a problem, if store heavly in hash map, hash map should carry both the value and the link list node, which is not convinent, so we probaly use hashmap as a lookup or retrival layer that can local the node by key, then use LL to handle recent, use node to store 


    def __init__(self, capacity: int):
        self.cap = capacity
        self.memo = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def update_recent(self,key):
            curr = self.memo[key]
            # prev <-> next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            # move current to most recent
            curr.prev = self.head
            curr.next = self.head.next
            curr.next.prev = curr
            self.head.next = curr

    def get(self, key: int) -> int:
        
        if key in self.memo:
            self.update_recent(key)
            return self.memo[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        def remove_least_recent():
            if self.tail == self.head:
                return
            removing_node = self.tail.prev
            removing_node.prev.next = self.tail
            self.tail.prev = removing_node.prev
            del self.memo[removing_node.key]
        def insert_new_node():
            new_node = Node(key,value)
            self.memo[key] = new_node 
            new_node.next = self.head.next
            self.head.next.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
        
        
        if key not in self.memo:
            if len(self.memo) == self.cap:
                remove_least_recent()
            insert_new_node()
        #upsert memo
        self.memo[key].val = value
        self.update_recent(key)
        
