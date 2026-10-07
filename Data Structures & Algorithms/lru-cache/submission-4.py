class Node:
    def __init__(self, val, key):
        self.prev = self
        self.next = self
        self.val = val
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.tracker = {} #this will be key: Node which also will store the value storage
        self.capacity = capacity
        self.curr_cap = 0
        self.sent = Node(val = None, key = None) #start of the tracker for what we just used
        #if we use get or put, we have to move the key we just used to the tail, the most recenlty used thing. the head of this is the least recently used thing, and if we need to remove something, thats the thing we will remove
        

    def get(self, key: int) -> int:
        if key in self.tracker:
            #linked list rearranging, mvoe key to the tail of the linked list (mru position)
            tail = self.sent.prev
            k_node = self.tracker[key] #this is the node we need
            if k_node == tail:
                return self.tracker[key].val 
            p_k = k_node.prev
            a_k = k_node.next

            p_k.next = a_k
            a_k.prev = p_k
            k_node.prev = tail
            tail.next = k_node
            k_node.next = self.sent #k_node became the new tail
            self.sent.prev = k_node
            return self.tracker[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.tracker:
            self.tracker[key].val = value
            tail = self.sent.prev
            k_node = self.tracker[key] #this is the node we need 
            if k_node == tail:
                return
            p_k = k_node.prev
            a_k = k_node.next

            p_k.next = a_k
            a_k.prev = p_k
            k_node.prev = tail
            tail.next = k_node
            k_node.next = self.sent #k_node became the new tail
            self.sent.prev = k_node
        else: #new item being added
            self.curr_cap += 1

            if self.curr_cap > self.capacity: #need to remove the least recenlty used (head of the sentinal)
            #if this key has already been used then we just need to mveo it back
            #otherwise we need to add a new node to the end of our lr tracker
                to_remove = self.sent.next
                self.tracker.pop(to_remove.key)
                after_to_remove = to_remove.next
                self.sent.next = after_to_remove
                after_to_remove.prev = self.sent
                
                self.curr_cap -= 1

            new_node = Node(val = value, key = key)
            tail = self.sent.prev
            tail.next = new_node
            new_node.prev = tail
            self.sent.prev = new_node
            new_node.next = self.sent
            self.tracker[key] = new_node
            if self.curr_cap == 1:
                self.sent.next = new_node

