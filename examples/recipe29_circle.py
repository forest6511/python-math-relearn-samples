from sympy import Eq, solve, symbols

y = symbols("y")

a, b, r = 2, 1, 3  # 中心(2, 1)、半径3

# 円の上で x = 2 のときの y を求める
x = 2
solutions = solve(
    Eq((x - a) ** 2 + (y - b) ** 2, r**2), y
)
print("x =", x, "のときの y:", solutions)
