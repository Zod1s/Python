from sympy import *
init_printing(use_latex=True)

x = symbols('x')
expr = 2 + I*x
pprint(re(expr))