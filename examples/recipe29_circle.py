"""レシピ29: 円の式 (x-a)^2 + (y-b)^2 = r^2 の上の点を求める。"""
from sympy import symbols, solve, Eq

y = symbols('y')
a, b, r = 2, 1, 3                # 中心(2,1)、半径3
x = 2
solutions = solve(Eq((x - a)**2 + (y - b)**2, r**2), y)
print("x =", x, "のときの y:", solutions)
