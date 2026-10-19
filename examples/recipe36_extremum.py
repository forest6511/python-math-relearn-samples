from sympy import diff, solve, symbols

x = symbols("x")

y = x**2 - 4 * x + 3  # 放物線 y = x² - 4x + 3
katamuki = diff(y, x)  # 傾きの式
print("傾きの式:", katamuki)

# 傾きが 0 になる x を探す（てっぺん・底の候補）
soko = solve(katamuki, x)
print("傾きが0になる x:", soko)
print("そのときの y:", y.subs(x, soko[0]))
