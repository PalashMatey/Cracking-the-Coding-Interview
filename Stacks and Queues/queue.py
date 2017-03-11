'''Queue implementation using node'''
class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class Queue(object):
    
    def __init__(self):
        self.length = 0
        self.head = None
    
    def isEmpty(self):
        return self.length == 0
    
    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length += 1
    
    def remove(self):
        if self.head is None:
            raise Exception('Queue is empty')
        cargo = self.head.data
        self.head = self.head.next
        self.length -= 1
        return cargo

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print q.remove()

'''Queue implementation using Lists '''
# class Queue(object):
#     def __init__(self):
#         self.queue = []
    
#     def isEmpty(self):
#         return self.size() == 0

#     def size(self):
#         return len(self.queue) 
    
#     def insert(self, cargo):
#         self.queue.append(cargo)
    
#     def remove(self):
#         if self.isEmpty():
#             raise Exception('Queue is Empty')
#         cargo = self.queue[0]
#         del self.queue[0]
#         return cargo
    
#     def peek(self):
#         if self.isEmpty():
#             raise Exception('Queue is Empty')
#         return self.queue[-1]
    

    
# q = Queue()
# q.insert(4)
# q.insert(5)
# print q.peek()
# print q.remove()
