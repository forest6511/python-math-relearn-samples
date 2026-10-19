from sympy import diff, symbols

x = symbols("x")

# x の3乗÷3 を微分すると、x の2乗に戻るか
print("x**3/3 を微分:", diff(x**3 / 3, x))

# おわり(1)を入れた値から、はじめ(0)を入れた値を引く
shiki = x**3 / 3
print(
    "1 と 0 で引くと:",
    shiki.subs(x, 1) - shiki.subs(x, 0),
)
