from Utils import MARKER, VAR, FUNCTIONS, ARG_0, ARG_1, ARG_2
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

    @staticmethod
    def is_valid(node):
        rep = []

        if node is not None:

            if node.left and node.right:
                if node.data in ARG_2:
                    rep += [True]
                else:
                    rep += [False]
            elif node.left and not node.right:
                if node.data in ARG_1:
                    rep += [True]
                else:
                    rep += [False]

            # elif not node.left and node.right:
            #         rep += [False]
            elif (not node.left) and (not node.right):
                if node.data == VAR:
                    rep += [True]
                else:
                    try:
                        float(node.data)
                        rep += [True]
                    except:
                        rep += [False]
            # else:
            #     rep += [False]
            # if rep[-1] == False:
            #     print("Validation failed with left = %s, right = %s, data = %s" % (node.left, node.right, node.data))

            rep += Tree.is_valid(node.left)
            rep += Tree.is_valid(node.right)

        return rep

