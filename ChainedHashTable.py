from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        bin = self._hash(key)
        
        # Iterates through the List stored at the node with the matched Hash Value
        for i in range(self.t[bin].size()):
            if self.t[bin].get(i).key == key:     # If the key of the current item matches the desired key,
                return self.t[bin].get(i).value   # Return the value stored in the current item
        
        # Returns "None" when unable to find node with desired key
        return None
        

    def add(self, key: object, value: object):
        # PRECONDITION - check for any items with same key
        if self.find(key) is not None:
            return False
        
        # INVARIANT - n <= len(t) <= 3n
        if self.n == len(self.t):
            self.resize()
        
        bin = self._hash(key)
        
        # Create a new item and add it to the front of the List at the selected bin
        item = self.Node(key, value)
        self.t[bin].add(0, item)
        
        # Increment n by 1
        self.n += 1
        
        return True


    def remove(self, key: int) -> object:
        bin = self._hash(key)
        
        for i in range(self.t[bin].size()):
            if self.t[bin].get(i).key == key:
                """ 
                1) Remove the item
                2) Decrement n by 1
                3) INVARIANT - n <= len(t) <= 3n --> Resize
                4) Return True --> method was successful
                """
                self.t[bin].remove(i)
                self.n -= 1
                if len(self.t) > 3 * self.n:
                    self.resize()
                return True
        
        return None     # Returns false if remove(key) is unsuccessful


    def resize(self):
        
        if self.n == len(self.t):   # Upsizing
            self.d += 1
        else:                       # Downsizing
            self.d -= 1
        
        # Create a temp table to store all the values
        tempTable = self.alloc_table(2**self.d)
        
        # Iterate through all the bins in the table
        for table in range(len(self.t)):
            # Iterate through all the items in the current bin
            for index in range(self.t[table].size()):
                # Add the current item to the temp table
                bin = self._hash(self.t[table].get(index).key)
                tempTable[bin].add(0, self.t[table].get(index))
        
        # Override current table with temp table
        self.t = tempTable
                
            
    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
