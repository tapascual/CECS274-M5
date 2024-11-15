from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        
        # Create new node with given key and value
        newNode = self.Node(key, value)
        
        # Find the node that will be the parent of the new node
        parent = self._find_last(key)
        
        # Make new node the child of the parent
        child = self._add_child(parent, newNode)
        return child


    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        
        node = self._find_eq(key)
        if node is None:    # If the node doesn't exist, return NIL
            return None
        
        return node.v


    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        
        # Find node with given key
        u = self._find_eq(key)
        
        # If there is no node with the given key, raise Error
        if u is None:
            raise ValueError
        
        # Store value in temp var, remove the node, then return value
        value = u.v
        self._remove_node(u)
        return value


    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        # Let current be the root
        current = self.r
        
        # Iterate until the current node does not exist
        while current is not None:
            
            # Verify if the key is >,<, or == to current.key
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        
        # Return NIL when no node has the given key
        return None


    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        current = self.r
        parent = None
        
        while current is not None:
            
            parent = current
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
            
        return parent


    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        # PRECONDITION --> set root to u if parent node doesn't exist
        if p is None:
            self.r = u
            
        # Determine the positioning of u
        else:
            
            # u is left child of p
            if u.k < p.k:
                p.left = u
            
            # u is right child of p
            elif u.k > p.k:
                p.right = u
            
            # key already exists --> return false
            else:
                return False
            
            # Set p as the parent of u
            u.parent = p
        
        # Increment n by 1 and return true 
        self.n += 1
        return True


    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u has at most one child
        """
        
        # Initialize child to be the child of 'u'
        if u.left is not None:
            child = u.left
        else:
            child = u.right
            
        # If u is the root, make child the root and set parent of u to NIL
        if u is self.r:
            self.r = child
            p = None
        # Else, make p the parent of u
        else:
            p = u.parent
            if p.left == u:
                p.left = child
            else:
                p.right = child
        
        # If child is not null, assign p to child.parent
        if child is not None:
            child.parent = p
        
        # Decrement n by 1
        self.n -= 1
        


    def _remove_node(self, u: BinaryTree.Node):
        # If u has a child, splice u
        if u.left is None or u.right is None:
            self._splice(u)
        else:
            # Find the node with the largest key before u.k
            w = u.right
            while w.left is not None:
                w = w.left
            
            # Override the key and value of u with the node with the key that was found
            u.k = w.k
            u.v = w.v 

            self._splice(w)
            
    
    def findKeyOrSmallest(self, key: object) -> BinaryTree.Node:
        """
        Returns node containing the given key
        If no node contains the key, returns node with smallest key greater than given key
        """
        
        # Set current to root and temp var to none
        current = self.r
        smallest = None
        
        # Iterates until the current node is NIL
        while current is not None:
            if key < current.k:
                smallest = current
                current = current.left
                
            elif key < current.k:
                current = current.right
                
            else:
                return current
            
        return smallest
        


    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0


    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)


    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w


    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
