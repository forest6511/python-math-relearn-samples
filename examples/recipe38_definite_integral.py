from sympy import integrate, symbols

x = symbols("x")  # x を「文字」として用意

# y = x の2乗 を、0 から 1 まで積分（下の面積を出す）
menseki = integrate(x**2, (x, 0, 1))
print("0から1までの面積:", menseki)
