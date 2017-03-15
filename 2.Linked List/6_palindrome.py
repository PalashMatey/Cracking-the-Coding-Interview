
class ListNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList(object):
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
        while(temp):
            print temp.data,
            temp = temp.next

    def palindromeLinkedList(self,l1):
        
        fast = slow = l1.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            current = slow.next
            slow.next = prev
            prev = slow
            slow = current
        
        while prev:
            if prev.data != l1.head.data:
                print 'False'
                return
            prev = prev.next
            l1.head = l1.head.next
        print 'True'



ll = LinkedList()

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(1)
ll.print_linkedList()
ll.palindromeLinkedList(ll)

            
