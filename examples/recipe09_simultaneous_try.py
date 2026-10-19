from sympy import Eq, solve, symbols

x, y = symbols("x y")
shiki1 = Eq(y, x + 1)
shiki2 = Eq(y, -x + 7)
print(solve([shiki1, shiki2], [x, y]))
