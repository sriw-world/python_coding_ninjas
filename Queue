#### Reverse a Queue

####using stack
def reverseQueue(inputQueue) :
    l = []
    while not inputQueue.empty():
        l.append(inputQueue.queue[0])
        inputQueue.get()
    
    while len(l) != 0:
        inputQueue.put(l.pop())
        
    return inputQueue

### using recurrsion
def reverseQueue(inputQueue) :
    
    if  inputQueue.qsize() <=1:
        return
    front = inputQueue.get()
    reverseQueue(inputQueue)
    inputQueue.put(front)


##################Reverse the First K Elements in the Queue

def reverseKElements(inputQueue, k) :
    q1 = queue.Queue()
    while k>0:
        q1.put(inputQueue.get())
        k-=1

    reverse(q1)
    while not inputQueue.empty():
        q1.put(inputQueue.get())
    
    return q1
    
    
def  reverse(subQueue):
    if subQueue.qsize() <=1:
        return
    
    front = subQueue.get()
    reverse(subQueue)
    subQueue.put(front)
    
    
    
    ############## Queue using LL
class Queue :
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def getSize(self) :
        return self.count

    def isEmpty(self) :
        return self.getSize() == 0
            
    def enqueue(self, data) :
        if self.head == None :
            newnode = Node(data)
            self.head = newnode
            self.tail = newnode
            self.count += 1
        else:
            newnode = Node(data)
            self.tail.next = newnode
            self.tail = newnode
            self.count += 1

    def dequeue(self) :
        if self.head == None:
            return -1
        head1 = self.head
        self.head = self.head.next
        head1.next = None
        self.count -= 1
        return head1.data

    def front(self) :
        if self.head == None:
            return -1
        return self.head.data
        
        
        
#########Stack using Queue
class Stack :
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.count = 0

    def getSize(self) :
        return self.count
    
    def isEmpty(self) :
        return self.getSize() == 0
    
    def push(self, data) :
        self.q2.put(data)
        while not self.q1.empty() :
            self.q2.put(self.q1.queue[0])
            self.get()
        
        self.q1,self.q2 = self.q2, self.q1
        self.count += self.count
        
        
    def pop(self):
        if (self.q1.empty()):
            return
        self.count -= self.count
        return self.q1.get()
    
    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]
  
  
  
  ####Queue using stack
  class Queue:  
    def __init__(self): 
        self.s1 = [] 
        self.s2 = [] 
  
    def enQueue(self, x): 
          
        # Move all elements from s1 to s2  
        while len(self.s1) != 0:  
            self.s2.append(self.s1[-1])  
            self.s1.pop() 
  
        # Push item into self.s1  
        self.s1.append(x)  
  
        # Push everything back to s1  
        while len(self.s2) != 0:  
            self.s1.append(self.s2[-1])  
            self.s2.pop() 
  
    # Dequeue an item from the queue  
    def deQueue(self): 
          
            # if first stack is empty  
        if len(self.s1) == 0:  
            print("Q is Empty") 
      
        # Return top of self.s1 
        return self.s1.pop()  



    
    
