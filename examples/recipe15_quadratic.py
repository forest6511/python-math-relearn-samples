"""レシピ15: 二次方程式の解 = 放物線とx軸が交わる点。"""
from sympy import symbols, solve, Eq

x = symbols('x')  # x を文字として用意する

# x の2乗 - x - 6 = 0 を解く（** は「2乗」の意味）
print(solve(Eq(x**2 - x - 6, 0), x))
