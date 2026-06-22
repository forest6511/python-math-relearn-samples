"""レシピ36: 傾きが0になる場所＝山のてっぺん・谷の底（極値）。"""
from sympy import symbols, diff, solve

x = symbols('x')
y = x**2 - 4*x + 3
katamuki = diff(y, x)
soko = solve(katamuki, x)                # 傾きが0になる x
print("傾きが0になる x:", soko)
print("そのときの y:", y.subs(x, soko[0]))
