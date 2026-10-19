from sympy import Eq, solve, symbols

y = symbols("y")
a, b, r = 2, 1, 5  # 半径を 5 に大きくした
x = 2
solutions = solve(
    Eq((x - a) ** 2 + (y - b) ** 2, r**2), y
)
print("x =", x, "のときの y:", solutions)
