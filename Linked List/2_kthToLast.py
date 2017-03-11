
class ListNode:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        node = ListNode(data)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def getData(self):
        return self.getData
    
    def getNext(self):
        return self.next
    
    def setData(self,newData):
        self.data = newData

    def print_linkedList(self):
        temp = self.head
        print '\n'
        while(temp):
            print temp.data,
            temp = temp.next
    
    def removeKthToLast(self,k):
        slow = fast = self.head
        for _ in range(k):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        self.print_linkedList()
    
    def getKthToLast(self , k):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        elementToReach = count - k
        prev = None
        current = self.head
        countNew = 0
        while current:
            countNew += 1
            if countNew == elementToReach:
                if count %2 == 0:
                    return current.data
                else:
                    return current.next.data
            current = current.next
        
        
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.print_linkedList()
ans = ll.getKthToLast(3)
print '\nThe kth to last element is: ',ans



