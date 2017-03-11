from collections import deque
class Stack(object):

    def __init__(self):
        self._queue = deque()
    
    def push(self,cargo):
        q = self._queue
        q.append(cargo)
        for _ in range(len(q)-1):
            q.append(q.popleft())
    
    def pop(self):
        return self._queue.popleft()
    
    def top(self):
        return self._queue[0]
    
    def empty(self):
        return len(self._queue) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()