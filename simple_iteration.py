from cmath import asin
from math import asinh, tanh

def simple_iteration_method(f, a, b, eps):
    x = (a + b) / 2
    _x = a
    n = 0
    phi = lambda x: asinh(12*tanh(x) + 0.311)
    while(abs(x - _x) > 1.5*eps):
        n += 1
        _x = x
        print(f'x{n - 1} = {_x}')
        x = phi(_x)
    
    print(f'x{n} = {x}')
    print(f'The root of the equation f(x) = 0 is {x}')
    print(f'The posterior number of steps is {n}')