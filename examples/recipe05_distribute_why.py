from sympy import simplify, symbols

x = symbols("x")

print(simplify(3 * x + 2 * x))  # 3x と 2x をまとめる
# x の仲間と数の仲間を、別々にまとめる
print(simplify(2 * x + 5 + 3 * x + 1))
