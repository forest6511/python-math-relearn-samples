"""レシピ34: 微分。2点を近づけると割線が接線の傾きに近づく。"""
def y(x):
    return x ** 2

for h in [1.0, 0.5, 0.1, 0.01, 0.001]:
    katamuki = (y(1 + h) - y(1)) / h
    print(f"h = {h}: 傾き = {round(katamuki, 4)}")
