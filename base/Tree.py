from Utils import MARKER, VAR, FUNCTIONS
from matplotlib import pyplot as plt
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
    def createTree(self, code):
        """function creating a new branch"""
        if(not code or code[0] == MARKER):
            code.pop(0)
            return
        object = self;
        object.data = code[0]
        print(object.data)

        code.pop(0)
        object.left = Tree()
        object.left.createTree(code)
        object.right = Tree()
        object.right.createTree(code)
    def calculate(self, x):
        if (not self.left) and (not self.right):
            if self.data != VAR:
                return float(self.data)
            else:
                return x
        elif self.left and self.right:
            return FUNCTIONS[self.data](self.left.calculate(x), self.right.calculate(x))
        else:
            return FUNCTIONS[self.data](self.left.calculate(x))
drzefko = Tree()
kod = ['sin', '+', 'x', '$', '$', '*', 'x', '$', '$', '4', '$', '$', '$']
drzefko.createTree(kod)
print(kod)
y = []
for ii in range(0,100):
    y.append(drzefko.calculate(ii/100))
plt.plot(y)
plt.show()