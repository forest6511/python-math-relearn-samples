from sympy import Eq, solve, symbols

x, y = symbols("x y")  # x と y を文字として用意する

# 2本の式（2直線）を用意する
shiki1 = Eq(y, x + 1)  # y = x + 1
shiki2 = Eq(y, -x + 5)  # y = -x + 5

# 2本を同時に満たす x と y を求める
print(solve([shiki1, shiki2], [x, y]))
