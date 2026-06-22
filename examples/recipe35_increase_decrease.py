"""レシピ35: 傾きの符号でグラフの上り下り（増減）を読む。"""
from sympy import symbols, diff

x = symbols('x')
y = x**2 - 4*x                           # 放物線
katamuki = diff(y, x)                    # 傾きの式
print("傾きの式:", katamuki)
for ten in [0, 1, 2, 3, 4]:
    print(f"x={ten} の傾き:", katamuki.subs(x, ten))
