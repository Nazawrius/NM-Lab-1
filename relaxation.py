def relaxation_method(f, a, b, eps):
    x = (a + b) / 2
    _x = a
    tau = 0.0537
    n = 0
    while(abs(x - _x) > eps):
        n += 1
        _x = x
        print(f'x{n - 1} = {_x}')
        x = _x - tau * f(_x)
    
    print(f'x{n} = {x}')
    print(f'The root of the equation f(x) = 0 is {x}')
    print(f'The posterior number of steps is {n}')