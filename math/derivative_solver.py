from sympy import *
init_printing(use_unicode=True)
x, y, z, t, k= symbols('x y z t k')
n = symbols('n', integer=True)
f, g, N = symbols('f g N', cls=Function)

# expr = (x**2 - 4 * x) * exp(-1/(x**2 - 4 * x))
# pprint(limit(expr/x**2, x, oo))
# an = cos(n) * sin(1/n)# log(1 + sin(1/n)**2) - (exp(1/n) - 1) * sin(1/n) # + 1 / (2 * n**4)
# expr = Sum(an, (n,1,oo))
# pprint(expr.is_absolutely_convergent())
# expr = x * log(x) * exp(x)
# pprint(integrate(expr, x))

# pprint(simplify((x**2 - 4*x -5)/(2*x + 2)))

# expr = f(x).diff(x) + 3 * log(x + 1) * f(x)
# sol = dsolve(expr, f(x), ics={f(0):1})
# pprint(sol)
# func = sol.rhs
# pprint(func.subs(x, 0))
# p1 = plotting.plot(exp(x) * log(x + 1), show=False)
# p1.show()

# expr = (x + 1) * exp(-x)
# pprint(simplify(expr.diff(x,x)))

# expr = acos((cos(x))/(1 + 2*cos(x)))
# pprint(expr)
# pprint(integrate(expr, (x,0,pi/2)))

# f1 = 2 * x * exp(-3 * x**2)
# pprint(f1.subs(x, 1 / sqrt(3)))

# f = v / sqrt(1 - (v**2 / c**2)) - L/t
# pprint(f.subs([(L, 4.24e8), (t, 1), (c, 3e8), (v, 0.816327075 * 3e8)]))
# pprint(solveset(f,v))

# x = sqrt(8) * (cos(pi/4) + I * sin(pi/4))
# pprint(solveset(z**3 - x, z))
# x = root(8, 6) * (cos(2 * 2 * pi / 3 + pi / 12) + I * sin(2 * 2 * pi / 3 + pi / 12))
# pprint(simplify(x))
# pprint(Abs(x - I)**2)
# x = 2 * I + 2
# pprint(nonlinsolve([z**3 - x, Abs(z - I)**2 - 1], [z]))

expr = (1 - x) * exp(1 / (2 * x + 2))
# expr2 = log(abs(1/sin(x) - cos(x)/sin(x)))
pprint(simplify(expr.diff(x)))
