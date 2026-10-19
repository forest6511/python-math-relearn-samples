from sympy import expand, symbols

x = symbols("x")
a = -2  # 傾きをマイナスに（右下がりの線）
x1, y1 = 0, 5  # 通る点を (0, 5) に
y = a * (x - x1) + y1
print("直線の式: y =", expand(y))
