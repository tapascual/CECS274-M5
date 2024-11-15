from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:

        # PRECONDITION
        if i < 0 or i > self.n:
            return None
        
        # Create a temp node to store data
        tempNode = self.Node(None)
        
        # Check if index is in first half
        if i < (self.n / 2) :
            tempNode = self.dummy.next # Start at head
            for j in range(i):  # Iterate forward i times
                tempNode = tempNode.next
        
        # When index is in second half
        else:
            tempNode = self.dummy   # Start at tail
            for j in range(self.n - i): # Iterate backwards n-i times
                tempNode = tempNode.prev
        
        return tempNode


    def get(self, i) -> object:
        
        # PRECONDITION
        if i < 0 or i >= self.n:
            raise Exception
        
        return self.get_node(i).x


    def set(self, i: int, x: object) -> object:

        # PRECONDITION
        if i < 0 or i >= self.n:
            raise Exception
        
        tempNode = self.get_node(i)

        # Store the data of i into a temp var
        data = tempNode.x

        # Override data of node i with new data 'x'
        tempNode.x = x
        
        # Return overriden data
        return data


    def add_before(self, w: Node, x: object) -> Node:

        # PRECONDITION
        if w is None:
            raise Exception
        
        # Recall Diagram in notes
        tempNode = self.Node(x)
        tempNode.prev = w.prev
        tempNode.next = w
        w.prev = tempNode
        tempNode.prev.next = tempNode

        # Incremenet n by 1
        self.n += 1

        return tempNode


    def add(self, i: int, x: object):
        
        # PRECONDITION
        if i < 0 or i > self.n:
            return Exception
        
        return self.add_before(self.get_node(i), x)
    

    def _remove(self, w: Node):

        # Store data in temp before removal
        tempNode = w

        # Cut connections to node 'w'
        w.prev.next = w.next
        w.next.prev = w.prev

        # Decrement n by 1
        self.n -= 1

        # Return data that was removed
        return tempNode.x


    def remove(self, i: int):
        if i < 0 or i >= self.n:  
            raise IndexError
        return self._remove(self.get_node(i))


    def size(self) -> int:
        return self.n


    def append(self, x: object):
        self.add(self.n, x)


    def isPalindrome(self) -> bool:
        
        tempNode = self.dummy.next
        word = ''
        
        while tempNode != self.dummy:
            char = tempNode.x.lower()
            if char .isalnum():
                word += char
            tempNode = tempNode.next
            
        return word == word[::-1]        


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
    
    def reverse(self):
        
        # Iterates towards the middle of the list, starting with the two ends and move inwards
        tempNode = self.dummy
        for i in range(self.n + 1):
            tempNode.next, tempNode.prev = tempNode.prev, tempNode.next     # Swaps the last and first nodes of the loop 
            tempNode = tempNode.prev
    
