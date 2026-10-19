from sympy import Eq, solve, symbols

x = symbols("x")
print(solve(Eq(x**2 - 2, 0), x))
