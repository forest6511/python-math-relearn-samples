def y(x):
    return x**2 - 4 * x + 1  # y = x^2 - 4x + 1 のルール


# 頂点 x=2 の前後の値を並べてみる
for x in [0, 1, 2, 3, 4]:
    print("x =", x, "のとき y =", y(x))
