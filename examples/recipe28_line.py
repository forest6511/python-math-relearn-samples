"""レシピ28: 直線を「傾きと通る点」から式に組み立てる。"""
from sympy import symbols, expand

x = symbols('x')
a = 3                            # 傾き
x1, y1 = 1, 2                    # 通る点 (1, 2)
y = a * (x - x1) + y1
print("直線の式: y =", expand(y))
