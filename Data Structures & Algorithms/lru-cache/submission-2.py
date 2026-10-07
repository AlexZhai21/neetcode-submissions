class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tracker = {}
        self.node_tracker = {} #key: Node for that key
        self.curr_cap = 0
        self.sent = Node(val = None)
        self.sent.prev = self.sent
        self.sent.next = self.sent #most recently used one would be sent.prev
        #least recently used one would be self.next
        

    def get(self, key: int) -> int:
  
        if key in self.tracker: #this means this is smth we have (and will thus also be trakced ino our list)

            get_Node = self.node_tracker[key]
            tail = self.sent.prev
            if tail.val != key:
                before = get_Node.prev
                after = get_Node.next
                before.next = after
                after.prev = before
                get_Node.prev = tail
                get_Node.next = self.sent
                tail.next = get_Node
                self.sent.prev = get_Node 
            #this complicated mess moves get_Node to the tial, making it the most recently used thing
            return self.tracker[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.tracker:
            # get_Node = self.node_tracker[key]
            # before = get_Node.prev
            # after = get_Node.next
            # before.next = after
            # after.prev = before
            # get_Node.prev = self.sent.prev
            # get_Node.next = self.sent
            # self.sent.prev.next = get_Node
            # self.sent.prev = get_Node
            get_Node = self.node_tracker[key]
            tail = self.sent.prev
            if tail.val != key:
                before = get_Node.prev
                after = get_Node.next
                before.next = after
                after.prev = before
                get_Node.prev = tail
                get_Node.next = self.sent
                tail.next = get_Node
                self.sent.prev = get_Node 

        if key not in self.tracker:
            self.curr_cap += 1
            new_new = Node(val = key)
            self.node_tracker[key] = new_new
            curr_tail = self.sent.prev
            new_new.prev = curr_tail
            new_new.next = self.sent
            curr_tail.next = new_new
            self.sent.prev = new_new
        self.tracker[key] = value
       
        
        if self.curr_cap > self.capacity:
            self.tracker.pop(self.sent.next.val)
            self.node_tracker.pop(self.sent.next.val)
            new_head = self.sent.next.next
            self.sent.next = new_head
            new_head.prev = self.sent
            self.curr_cap -= 1

        
