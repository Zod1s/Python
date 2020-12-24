from sympy import *
init_printing(use_unicode=True)
x, y, z, t, k = symbols('x y z t k', real=True)
n = symbols('n', integer=True)
f, g, N = symbols('f g N', cls=Function)

# expr = (1 - cos(x**2)) / (x * (x - sin(x)) - x**3 * (sin(x))**2)
# pprint(limit(expr, x, 0))
# an = cos(n) * sin(1/n)# log(1 + sin(1/n)**2) - (exp(1/n) - 1) * sin(1/n) # + 1 / (2 * n**4)
# expr = Sum(an, (n,1,oo))
# pprint(expr.is_absolutely_convergent())
# expr = log(abs(exp(2 * x) * (1 - exp(2 - 2 * x)))) - 2 * x
# pprint(limit(expr, x, oo))
# an = n**(1/3) / (sqrt(n**2 + n + 1))
# expr = Sum(an, (n,1,oo))
# pprint(expr.is_convergent())
# expr = atan(x)# cos(sqrt(2*x))
# pprint(simplify(expr.diff(x, 4))) # .subs(x, pi/8).evalf())
# expr = log(1 + sin(x))
# pprint(series(expr, x, 0, 4))

# expr1 = 1 / abs(sin(x)) - 1 / abs(log(1 + sqrt(abs(x))))
# expr2 = exp(1 / abs(x)) + log(abs(x)) / x**3
# expr3 = (exp(sin(x)) - 1 - sin(x)) / ((tan(x))**2 * (sinh(x) - x))
# expr4 = log(1 + x) / (sin(x) * (1 - cos(x)))
# pprint(limit(expr1 / expr2, x, 0))
# pprint(limit(expr1 / expr3, x, 0))
# pprint(limit(expr1 / expr4, x, 0))
# expr = x*2**x / 5**x# (2**x - 2**(x*log(x))) / (x**x)
# pprint(limit(expr, x, oo))
# pprint(limit(expr4, x, 0))

# expr = f(x).diff(x) + 3 * log(x + 1) * f(x)
# sol = dsolve(expr, f(x), ics={f(0):1})
# pprint(sol)
# func = sol.rhs
# pprint(func.subs(x, 0))
# p1 = plotting.plot(exp(x) * log(x + 1), show=False)
# p1.show()

# expr = (x + 1) * exp(-x)
# pprint(simplify(expr.diff(x,x)))
# f1 = 2 * x * exp(-3 * x**2)
# pprint(f1.subs(x, 1 / sqrt(3)))

# f = v / sqrt(1 - (v**2 / c**2)) - L/t
# pprint(f.subs([(L, 4.24e8), (t, 1), (c, 3e8), (v, 0.816327075 * 3e8)]))
# expr = x**2 + 3 * x - I
# pprint(solveset(expr, x))

# x = sqrt(8) * (cos(pi/4) + I * sin(pi/4))
# pprint(solveset(z**3 - x, z))
# x = root(8, 6) * (cos(2 * 2 * pi / 3 + pi / 12) + I * sin(2 * 2 * pi / 3 + pi / 12))
# pprint(simplify(x))
# pprint(Abs(x - I)**2)
# x = 2 * I + 2
# pprint(nonlinsolve([z**3 - x, Abs(z - I)**2 - 1], [z]))

# expr = (1 - x) * exp(atan(4/x))
# expr2 = log(abs(1/sin(x) - cos(x)/sin(x)))
# pprint(simplify(expr.diff(x,2)))

# a = 0
# expr = (log(x + 3) - log(x + 1) - sin(2 / x)) / (cos(sin(1 / (2 * x))) - exp(a / x**2) - exp(-x))
# pprint(limit(expr, x, oo))