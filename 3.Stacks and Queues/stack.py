''' Stack Implementation using Node''''

class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
class Stack(object):
    def __init__(self,top = None):
        self.top = top
    
    def push(self,data):
        self.top = Node(data,self.top)
    
    def pop(self):
        if self.top is None:
            raise Exception('Stack is Full')
        value = self.top.data
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.top is None:
            raise Exception('Stack is Empty')
        return self.top.data
    
    def isEmpty(self):
        return self.top == None
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
print s.pop()
print s.peek()


        


''' Implemented Stack using Lists '''
# class Stack:
#     def __init__(self):
#         self.items = []
    
#     def isEmpty(self):
#         return self.items == []
    
#     def push(self, data):
#         self.items.append(data)
    
#     def pop(self):
#         if self.isEmpty():
#             raise Exception('Stack is Empty')
#         value = self.items[len(self.items)-1]
#         del self.items[len(self.items)-1]
#         return value
            
#     def peek(self):
#         return self.items[len(self.items)-1]
    
#     def size(self):
#         return len(self.items)

# s = Stack()
# s.push(2)
# s.push(3)
# s.push(4)
# s.pop()

# print s.peek()

# s.pop()

# print s.peek()