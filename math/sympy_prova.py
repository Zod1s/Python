# from sympy.physics.hydrogen import Psi_nlm
# from sympy import Symbol, init_printing, pprint
# init_printing(use_unicode=True)
# r = Symbol("r", real=True, positive=True)
# phi = Symbol("phi", real=True)
# theta = Symbol("theta", real=True)
# Z = Symbol("Z", positive=True, integer=True, nonzero=True)
# psi = Psi_nlm(2,0,0,r,phi,theta,Z)
# pprint(psi)
from sympy import *
init_printing(use_latex=True)
x, y, z, t, a, b = symbols('x y z t a b')
f, g = symbols('f g', cls=Function)
#expr = Derivative(f(x), x, x) + 9 * f(x)
#pprint(dsolve(expr, f(x), ics={f(0):0, f(pi/2):-1}))
expr = (25 - 4*x)**(1/2)
pprint(expr.diff(x))