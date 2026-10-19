def f(x):
    return x**2  # 放物線 y = x の2乗


for n in [4, 10, 100, 1000]:
    haba = 1 / n  # 長方形1個分の横はば
    menseki = 0  # 面積の合計（最初は0）
    for i in range(n):
        x = i * haba  # i 番目の長方形の左はしの x
        # 高さ × はば をたしていく
        menseki += f(x) * haba
    print(f"長方形 {n} 個: 面積 = {round(menseki, 4)}")
