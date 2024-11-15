import SLLQueue
from Interfaces import Tree


class BinaryTree(Tree):
    class Node:
        def __init__(self, key: object = None, val: object = None):
            self.parent = self.left = self.right = None
            self.k = key
            self.v = val

        def set_key(self, x):
            self.k = x

        def set_val(self, v):
            self.v = v

        def insert_left(self, u):
            self.left = u
            self.left.parent = self
            return self.left

        def insert_right(self, u):
            self.right = u
            self.right.parent = self
            return self.right

        def __str__(self):
            return f"({self.k}, {self.v})"


    def __init__(self):
        self.r = None


    def depth(self, u: Node) -> int:
        # PRECONDITION
        if u is None:
            return -1
        
        # d is the number of edges
        d = 0
        currentNode = u
        
        # Iterate up through the tree until the loop reaches the root
        while currentNode != self.r:
            currentNode = currentNode.parent
            d += 1
        
        return d
        

    def height(self) -> int:
        return self._height(self.r)


    def _height(self, u: Node) -> int:
        # Base Case
        if u is None:
            return -1
        
        # Recursive (Reduction) step
        return 1 + max(self._height(u.left), self._height(u.right))
        

    def size(self) -> int:
        return self._size(self.r)


    def _size(self, u: Node) -> int:
        # Base Case
        if u is None:
            return 0
        
        # Recursive (Reduction) step
        return 1 + self._size(u.left) + self._size(u.right)


    def bf_order(self):     # Breadth-first
        # Create empty list and empty queue
        nodes = []
        q = SLLQueue.SLLQueue()
        
        # Add the root to the queue
        if self.r is not None:
            q.add(self.r)
            
        # Iterates until the queue is empty
        while q.size() > 0:
            # Add the current node to list then remove from queue
            u = q.remove()
            nodes.append(u)
            
            # Repeat the process for the children until leaf is reached
            if u.left is not None:
                q.add(u.left)
            if u.right is not None:
                q.add(u.right)
            
        return nodes


    def in_order(self) -> list:
        return self._in_order(self.r)


    def _in_order(self, u: Node) -> list:   # left, current, right
       # Create an empty list
       nodes = []
       
       #  Add all nodes from left subtree
       if u.left is not None:
           nodes.extend(self._in_order(u.left))
          
       # Add the current node    
       nodes.append(u)
    
       # Add all nodes from right subtree
       if u.right is not None:
            nodes.extend(self._in_order(u.right))
        
       return nodes


    def post_order(self) -> list:
        return self._post_order(self.r)


    def _post_order(self, u: Node):     # left, right, current
        # Create an empty list
        nodes = []
        
        # Add all nodes from left subtree
        if u.left is not None:
            nodes.extend(self._post_order(u.left))
        
        # Add all nodes from right subtree
        if u.right is not None:
            nodes.extend(self._post_order(u.right))
        
        # Add the current node
        nodes.append(u)
        
        return nodes


    def pre_order(self) -> list:
        return self._pre_order(self.r)


    def _pre_order(self, u: Node):
        # Create an empty list
        nodes = []
        
        # Add current node
        nodes.append(u)
        
        # Add all nodes from left subtree
        if u.left is not None:
            nodes.extend(self._pre_order(u.left))
        
        # Add all nodes from right subtree
        if u.right is not None:
            nodes.extend(self._pre_order(u.right))
            
        return nodes


    def __str__(self):
        nodes = self.bf_order()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)