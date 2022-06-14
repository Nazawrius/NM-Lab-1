from math import sinh, tanh

from dichotomy import dichotomy_method
from relaxation import relaxation_method
from simple_iteration import simple_iteration_method

f = lambda x: sinh(x) - 12*tanh(x) - 0.311
a = 3.0
b = 4.0
eps = 10**(-4)
dichotomy_method(f, a, b, eps)
relaxation_method(f, a, b, eps)
simple_iteration_method(f, a, b, eps)