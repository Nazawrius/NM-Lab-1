from math import floor, log2

def dichotomy_method(f, a, b, eps):
    x = (a + b) / 2
    _x = a
    n = 0
    while(abs(x - _x) > eps):
        n += 1
        _x = x
        print(f'x{n - 1} = {_x}')
        if f(a) * f(x) < 0:
            b = x
            x = (a + x) / 2
        elif f(a) * f(x) == 0:
            break
        else:
            a = x
            x = (x + b) / 2
    
    print(f'x{n} = {x}')
    print(f'The root of the equation f(x) = 0 is {x}')
    print(f'The posterior number of steps is {n}')
