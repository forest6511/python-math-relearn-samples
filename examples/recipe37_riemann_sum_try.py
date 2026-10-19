def f(x):
    return x**2


for n in [4, 10, 100, 1000]:
    haba = 1 / n
    menseki = 0
    for i in range(1, n + 1):  # 1 から n まで
        x = i * haba  # 右はしの x
        menseki += f(x) * haba
    print(f"長方形 {n} 個: 面積 = {round(menseki, 4)}")
