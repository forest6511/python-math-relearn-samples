from sympy import integrate, symbols

x = symbols("x")
# y=2x を 0 から 4 まで
menseki = integrate(2 * x, (x, 0, 4))
print("面積:", menseki)
