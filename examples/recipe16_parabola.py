# y = x の2乗 のルール
def y(x):
    return x**2


# x を -3 から 3 まで入れて y を見る
for x in range(-3, 4):
    print(x, "->", y(x))
