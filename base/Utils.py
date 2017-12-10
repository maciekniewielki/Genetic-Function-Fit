from numpy import sin, exp, log

MARKER = '$'
VAR = 'x'
VAL = 'value'
FUNCTIONS = {'+': lambda x, y: x+y, '-': lambda x, y: x-y, '*': lambda x, y: x*y, ':': lambda x, y: x/y,
             'sin': lambda x: sin(x), 'exp': lambda x: exp(x), 'log': lambda x: log(x)}


class InvalidParameterError(Exception):
    pass


OPERATORS = ['+', '-', '*', ':', 'sin', 'exp', 'log', VAR, VAL]
ARG_0 = [VAR, VAL]
ARG_1 = ['sin', 'exp', 'log']
ARG_2 = ['+', '-', '*', ':']
MAX_DEPTH = 5
MIN_VAL = 1
MAX_VAL = 20
INT = True