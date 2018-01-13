from Utils import MARKER, VAR, FUNCTIONS
import numpy as np
#import matplotlib.pyplot as plt
import random

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def createTree(self, code):
        """function creating a new branch"""
        if not code or code[0] == MARKER:
            code.pop(0)
            return
        object = self
        object.data = code[0]

        code.pop(0)
        object.left = Tree()
        object.left.createTree(code)
        if object.left.data is None:
            object.left = None
        object.right = Tree()
        object.right.createTree(code)
        if object.right.data is None:
            object.right = None

    def calculate(self, x):
        if (not self.left) and (not self.right):
            if self.data != VAR:
                return float(self.data)*np.ones(np.size(x))
            else:
                return x
        elif self.left and self.right:
            return FUNCTIONS[self.data](self.left.calculate(x), self.right.calculate(x))
        else:
            return FUNCTIONS[self.data](self.left.calculate(x))

    def get_random_list(self, depth, l):
        if depth == 0 or (self.left is None and self.right is None):
            return l
        else:
            if random.random() > 0.5:
                if self.left:
                    l.append("left")
                    return self.left.get_random_list(depth-1, l)
                else:
                    l.append("right")
                    return self.right.get_random_list(depth - 1, l)
            else:
                if self.right:
                    l.append("right")
                    return self.right.get_random_list(depth - 1, l)
                else:
                    l.append("left")
                return self.left.get_random_list(depth - 1, l)

    def delete_tree(self):
        self.left = None
        self.right = None
        self.data = None

    @staticmethod
    def traverse(node):
        rep = []
        if node is not None:
            rep += [node.data]
            rep += Tree.traverse(node.left)
            rep += Tree.traverse(node.right)
        else:
            rep += "$"
        return rep
#wykorzystanie drzefka
""" 
kod = "sin + x $ $ * x $ $ 4 $ $ $"
lista = kod.split()
print(lista)
drzefko = Tree()
drzefko.createTree(lista)
x = np.linspace(0, 2*np.pi, 1000)
y = drzefko.calculate(x)
plt.plot(x, y)
plt.show() 
"""