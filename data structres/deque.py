import logging
from collections import deque

logger = logging.getLogger(__name__)

class deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = []
        self.LastElement = 0
        self.FirstElement = 0
    
    def isEmpty(self):
        return self.LastElement == 0
        
    def isFull(self):
        return self.LastElement >= self.capacity

    def push(self, item):
        if self.isFull():
            logger.error("the deque is full")
        else:
            self.deque.append(item)
            self.LastElement += 1
            print(f"{item} has been pushed to the top of the deque")

    def pushLeft(self, item):
        if self.isFull():
            logger.error("the deque is full!!")
        else:
            self.deque.insert(self.FirstElement, item)
            self.LastElement += 1
            print(f"{item} has been added to the start of the deque")

    def pop(self):
        if self.isEmpty():
            logger.error("the deque is empty")
        else:
            self.deque.pop
            self.LastElement -= 1
            print(f"the last element of the deque has been removed")

    def popLeft(self):
        if self.isEmpty:
            logger.error("the deque is empty")
        else:
            self.deque.pop(self.FirstElement)
            self.LastElement -= 1
            print("the first element has been removed")

    def peek(self):
        if self.isEmpty():
            logger.error("the deque is empty (in the peek function)")
        else:
            print(f"the last element of the deque is {self.deque[self.LastElement - 1]}")

    def print(self):
        if self.isEmpty():
            logger.error("the deque is empty")
        else:
            try:
                i = 0
                while True:
                    print(f"the element at index {i} is: {self.deque[i]}")
                    i += 1
            except:
                print("the deque has been printed")
                
                     
        
d = deque(10)
d.push(17)
d.pushLeft(15)
d.push(3)
d.pushLeft(4)
d.peek()
d.print()