class Node(object):

    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Queue(object):

    def __init__(self,head=None, tail = None):
        self.head = head
        self.tail = tail
        self.length = 0
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def dequeue(self):
        if self.head is None:
            raise Exception('Queue is Empty')
        else:
            value = self.head.data
            self.head = self.head.next
            self.length -= 1
            return value
    
    def peek(self):
        if self.head is None:
            raise Exception('Queue is Empty')
        return self.head.data
    
    def isEmpty(self):
        return self.head is None
    
    def getSize(self):
        return self.length
            

class Animal(object):

    def __init__(self, species, id = None):
        self.species = species
        self.id = id
    
    def setId(self,id):
        self.id = id
    
    def is_older_than(self,other):
        return self.id < other.id

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self,"Dog")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self,'Cat')

class AnimalQueue:

    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.id = 0
    
    def enqueue(self, animal):
        self.id += 1
        animal.setId(self.id)
        if isinstance(animal,Dog):
            self.dogs.enqueue(animal)
        elif isinstance(animal,Cat):
            self.cats.enqueue(animal)
        else:
            raise Exception('This shelter only accepts dogs and cats')

    def dequeueAny(self):
        if self.dogs.getSize() == 0 and self.cats.getSize() == 0:
            raise Exception('The shelter is Empty')
        if self.dogs.getSize() == 0:
            print 'There are no more dogs, you get a cat instead'
            return self.cats.dequeue()
        elif self.cats.getSize() == 0:
            print 'There are no more cats, you get a dog instead'
            return self.dogs.dequeue()
        else:
            dog = self.dogs.peek()
            cat = self.cats.peek()
            if dog.is_older_than(cat):
                print 'You got a Dog! ', dog.id
                return self.dogs.dequeue()
            else:
                print 'You got a cat ',cat.id
                return self.cats.dequeue()
    
    def dequeueDog(self):
        if self.dogs.getSize() == 0:
            raise Exception('There are no more Dogs in the shelter')
        print 'You got a dog'
        return self.dogs.dequeue()

    def dequeueCat(self):
        if self.cats.getSize() == 0:
            raise Exception('There are no more Cats in the shelter')
        print 'You got a Cat'
        return self.cats.dequeue()

a = AnimalQueue()
a.enqueue(Dog())
a.enqueue(Cat())
a.enqueue(Dog())
a.enqueue(Dog())
a.enqueue(Dog())
a.enqueue(Cat())
a.enqueue(Cat())
a.enqueue(Dog())
a.enqueue(Cat())
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueDog()
a.dequeueCat()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueDog()
a.dequeueDog()
