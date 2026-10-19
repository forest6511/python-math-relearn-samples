data = [(1, 40), (2, 50), (4, 62), (6, 78)]


# レシピA2 と同じ「誤差」の関数
def total_error(a, b):
    e = 0
    for hours, real in data:
        yosoku = a * hours + b  # その線での予測
        # 予測と実際のズレ（2乗してためる）
        e += (yosoku - real) ** 2
    return e


a = 5  # いまの傾き
b = 35
h = 0.01  # 傾きをほんの少しだけ動かす量

# 傾きを少し動かすと、誤差はどっちにどれだけ変化するか
henka = (total_error(a + h, b) - total_error(a, b)) / h
print("増やしたときの誤差の変化:", round(henka, 1))
if henka < 0:
    print("→ 誤差が減る。傾きは増やす方向へ直す")
else:
    print("→ 誤差が増える。傾きは減らす方向へ直す")
