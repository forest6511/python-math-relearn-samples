from sympy import diff, symbols

x = symbols("x")

y = x**2 - 4 * x  # 放物線 y = x² - 4x
katamuki = diff(y, x)  # 傾きの式（導関数）
print("傾きの式:", katamuki)

# いろいろな場所で傾きの符号を見る
for ten in [0, 1, 2, 3, 4]:
    print(f"x={ten} の傾き:", katamuki.subs(x, ten))
