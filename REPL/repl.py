import IPython
from sympy import (Derivative, integrate, symbols, var, dsolve, solve, solveset, init_printing, pprint, log, exp, simplify, Function, sin, cos, tan, asin, acos, atan,
sqrt, pi, oo)

funcs = {"derivative": Derivative,
         "integral": integrate,
         "symbols": symbols,
         "var": var,
         "dsolve": dsolve,
         "solve": solve,
         "solveset": solveset,
         "initprint": init_printing,
         "pprint": pprint,
         "ln": log,
         "exp": exp,
         "simpl": simplify,
         "func": Function,
         "sin": sin,
         "cos": cos,
         "tan": tan,
         "asin": asin,
         "acos": acos,
         "atan": atan,
         "sqrt": sqrt,
         "pi": pi,
         "inf": oo}


IPython.start_ipython(argv=[], user_ns=funcs)
