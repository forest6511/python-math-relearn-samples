from sympy import Eq, solve, symbols

x = symbols("x")  # x を文字として用意する

# x の2乗 - x - 6 = 0 を解く（** は「2乗」の意味）
print(solve(Eq(x**2 - x - 6, 0), x))
