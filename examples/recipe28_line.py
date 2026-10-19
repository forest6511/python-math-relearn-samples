from sympy import expand, symbols

x = symbols("x")

a = 3  # 傾き（線の急さ）
x1, y1 = 1, 2  # 通る点 (1, 2)

# 点(x1, y1)を通り、傾きaの直線の式を組み立てる
y = a * (x - x1) + y1
print("直線の式: y =", expand(y))
