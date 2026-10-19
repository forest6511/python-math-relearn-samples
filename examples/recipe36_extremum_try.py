from sympy import diff, solve, symbols

x = symbols("x")
y = -(x**2) + 6 * x  # 山型の放物線
katamuki = diff(y, x)
teppen = solve(katamuki, x)
print("傾きが0になる x:", teppen)
print("そのときの y:", y.subs(x, teppen[0]))
