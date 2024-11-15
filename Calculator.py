import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator
import re

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable()

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :

        stack = ArrayStack.ArrayStack()
        for i in s:
            if i =='(' :
                stack.push('(')
            elif i == ')':
                try: 
                    stack.pop()  
                except IndexError: 
                    return False
        size = stack.size()
        if size == 0:
            return True
        else:
            return False


    def _build_parse_tree(self, exp : str) ->str:
        if not self.matched_expression(exp):
            raise ValueError
        tree = BinaryTree.BinaryTree()
        tree.r = BinaryTree.BinaryTree.Node()
        current = tree.r
        split = re.split(r"(\W)", exp)
        expression = [x for x in split if x != '' and x != ' '] # Ignores variable name
        for token in expression:
            node = BinaryTree.BinaryTree.Node()
            
            if token == '(':
                # Add a left child to current
                current.insert_left(node)
                # Set current to left child
                current = current.left
                
            elif token == '+' or token == '-' or token == '/' or token == '*':
                current.set_val(token)
                current.set_key(token)
                # Add right child to current
                current.insert_right(node)
                # Set current to right child
                current = current.right
                
            elif token == ')':
                # Set current to parent node
                current = current.parent
            
            # Else, when token is a variable
            else: 
                current.set_key(token)
                current.set_val(self.dict.find(token)) # chainedHashTable storing variable with associated values
                current = current.parent
                
        return tree
        

    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        
        # Check if root is an operator
        if root.left is not None and root.right is not None:
            op = op[root.k]
            return op(self._evaluate(root.left), self._evaluate(root.right))
        
        # Check if root is a variable and is a leaf
        elif root.left is None and root.right is None:
            
            # If root doesn't have a key
            if root.k is None:
                raise ValueError("Missing right operand.")
            
            # If root has a key
            elif root.k is not None:
                return float(root.v)
            
            else:
                raise ValueError(f"Missing definition for variable {root.k}")
            
        elif root.left is not None:
            return self._evaluate(root.left)
        
        else:
            return self._evaluate(root.right)


    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)
    
    def print_expression(self, exp: str) :
        
        # Creates a list of variables found in the expression
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]    # Given as hint on Canvas
        
        # Creates list of tokens (everything other than the variables)
        everything_else = re.split('\w+', exp)    # Given as hint on Canvas
        
        result = ''
        
        # Concate into one string (result var)
        for i in range(len(everything_else)):
            result += everything_else[i]
            
            # Verifies loop variable is within the range of list of variables stored
            if i < len(variables):
                value = self.dict.find(variables[i])    # Find the value of the variable with the given key
                
                if value is not None:   # Verifies if there is a value for the variable
                    result += str(value)
                    
                else:   # If there is no value, add the variable bc there is no value for the variable
                    result += variables[i]
                
        print(result)