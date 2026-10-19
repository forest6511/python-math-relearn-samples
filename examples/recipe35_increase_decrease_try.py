from sympy import diff, symbols

x = symbols("x")
y = -3 * x + 5  # 右下がりの直線
katamuki = diff(y, x)
print("傾きの式:", katamuki)
for ten in [0, 1, 2]:
    print(f"x={ten} の傾き:", katamuki.subs(x, ten))
