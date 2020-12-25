from sympy import Array, tensorproduct, init_printing, symbols, pprint, eye
x, y, z, t = symbols('x y z t')
init_printing(use_unicode=True)
A = Array([x, y, z, t])
B = Array([1, 2, 3, 4])
pprint(tensorproduct(A, B))