data = [(1, 40), (2, 50), (4, 62), (6, 78)]


def total_error(a, b):
    return sum(
        (a * h + b - real) ** 2 for h, real in data
    )


a = 5  # いまの傾き
b = 35
h = 0.01  # 傾きをほんの少しだけ動かす量

# 傾きを少し動かすと、誤差はどっちにどれだけ変化するか
henka = (total_error(a + h, b) - total_error(a, b)) / h
print(
    "傾きを少し増やしたときの誤差の変化:",
    round(henka, 1),
)

if henka < 0:
    print(
        "→ 増やすと誤差が減る。"
        "だから傾きは増やす方向へ直す"
    )
else:
    print(
        "→ 増やすと誤差が増える。"
        "だから傾きは減らす方向へ直す"
    )
