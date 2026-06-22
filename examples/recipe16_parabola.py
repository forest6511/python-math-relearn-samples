"""レシピ16: y=ax² は U字に曲がった線（放物線）。"""
def y(x):
    return x ** 2  # y = x の2乗 のルール

# x を -3 から 3 まで入れて y を見る
for x in range(-3, 4):
    print(x, "->", y(x))
