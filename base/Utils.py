from numpy import sin, exp, log

MARKER = '$'
VAR = 'x'
FUNCTIONS = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, ':': lambda x, y: x/y,
             'sin': lambda x: sin(x), 'exp': lambda x: exp(x), 'log': lambda x: log(x)}
class InvalidParameterError(Exception):
    pass
