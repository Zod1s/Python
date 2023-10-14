from sympy import *
# from sympy.solvers.ode.systems import dsolve_system
init_printing(use_unicode=True)

x, y, t, k = symbols('x y t k', real=True)
z = symbols('z', complex=True)
n = symbols('n', integer=True)
s = symbols('s', complex=True)
alpha, beta, gamma = symbols('alpha beta gamma', real=True)
f, g, N, u = symbols('f g N u', cls=Function)

m, ks, k1, k2, b, L, r = symbols('m ks k1 k2 b L r', real=True)

F = Matrix([
    [0, 1, 0],
    [-ks / m, -b / m, -sqrt(k1 * ks * L) / (m * k1)],
    [-r * sqrt(k1 * ks * L) / k1, 0, -r * (2 * k2 + L) / (2 * k1)]
])
G = Matrix([0, 0, 1])
H = Matrix([[1, 0, 0]])
pprint(F)
pprint(G)
pprint(H)

sIF = s * eye(3) - F
pprint(sIF)
pprint(simplify(expand(sIF.det())))
# pprint(sIF**-1)

Gs = simplify(H * (sIF**-1) * G)

pprint(Gs)
pprint(expand(Gs.subs(
    [(m, 0.27), (ks, 158e3), (k1, 29.92e-6),
     (k2, 4e-5), (b, 7.53), (L, 4e-3), (r, 6)]
)))

# k1 = 0.021
# m1 = -34.459
# s1 = 130.2474
# o1 = 725.088

# k2 = -1.021
# m2 = -140.258
# s2 = 88.2425
# o2 = 10.8237

# w1 = 1 + exp(-s1 * x) * (k1 * cos(o1 * x) + (m1 - k1 * s1) / o1 * sin(o1 * x)) + \
#     exp(-s2 * x) * (k2 * cos(o2 * x) + (m2 - k2 * s2) / o2 * sin(o2 * x))
# pprint(w1)

# expr = (x + 1) / (x**2 + 0.2 * x + 1)
# pprint(simplify(expr.diff(x, x)))

# expr = 7 / (4 * (x + 4)**2 * (x - 3)) - 3 / (4 * x * (x + 4) * (x - 3))
# pprint(factor(simplify(expr)))

# C = Curve([cos(t), sin(t)], (t, 0, pi/2))
# pprint(line_integrate(1, C, [x, y]))

# expr = u(t).diff(t, t) - 4 * u(t) - 4 * exp(-2 * t)
# pprint(dsolve(expr, 0, ics={u(0):-1, u(t).diff(t).subs(t, 0):1}))
# expr = (x**(3 * alpha) - 1 + (cos(x))**(x**alpha)) / (x**(2 + alpha))
# pprint(expr)
# pprint(limit(expr.subs(alpha, 1.0), x, 0, '+'))

# expr = 1 / (x * (1 - x))
# pprint(integrate(expr, x))

# expr = atan(x)
# pprint(expr.diff(x))

# eq1 = Eq(S(t).diff(t), -beta * I(t) * S(t))
# eq2 = Eq(I(t).diff(t), beta * I(t) * S(t) - gamma * I(t))
# eq3 = Eq(R(t).diff(t), gamma * I(t))

# pprint(eq1)
# pprint(eq2)
# pprint(eq3)

# eq1.subs([(beta, 1), (gamma, 1)])
# eq2.subs([(beta, 1), (gamma, 1)])
# eq3.subs([(beta, 1), (gamma, 1)])

# solutions = dsolve_system([eq1, eq2, eq3])
# pprint(solutions)

# a = 4
# expr = ((4 * cos(x) - a)**2 - 4 * x**4) / (x**4 * sin(x)**2)
# pprint(limit(expr, x, 0))
# an = cos(n) * sin(1/n)# log(1 + sin(1/n)**2) - (exp(1/n) - 1) * sin(1/n) # + 1 / (2 * n**4)
# expr = Sum(an, (n,1,oo))
# pprint(expr.is_absolutely_convergent())
# expr = x * (3 ** ((2 * x + 1) / (x**2 + 1)) - 1)
# pprint(limit(expr, x, oo))
# an = n**(1/3) / (sqrt(n**2 + n + 1))
# expr = Sum(an, (n,1,oo))
# pprint(expr.is_convergent())
# expr = atan(x)# cos(sqrt(2*x))
# pprint(simplify(expr.diff(x, 4))) # .subs(x, pi/8).evalf())
# expr = log(1 + sin(x))
# pprint(series(expr, x, 0, 4))

# expr = 1 / (x**4 + 4 * x**2 + 4)
# expr = sqrt(2) * tan(x)
# pprint(expr.diff())

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

# expr = (9 * x + 1) ** 2 - (x + 3)
# pprint(solveset(expr, x))
# x = root(8, 6) * (cos(2 * 2 * pi / 3 + pi / 12) + I * sin(2 * 2 * pi / 3 + pi / 12))
# pprint(simplify(x))
# pprint(Abs(x - I)**2)
# x = 2 * I + 2
# pprint(nonlinsolve([z**3 - x, Abs(z - I)**2 - 1], [z]))

# expr = (1 - x) * exp(atan(4/x))
# expr2 = log(abs(1/sin(x) - cos(x)/sin(x)))
# pprint(simplify(expr.diff(x,2)))

# expr = 1/3 * sqrt((x**2 + 2)**3)
# pprint(expr.diff())
