# (勉強時間, 実際に取った点数) のデータ4人分
data = [(1, 40), (2, 50), (4, 62), (6, 78)]


# 傾きaと切片bの線が、
# 実際のデータからどれだけズレているか
def total_error(a, b):
    e = 0
    for hours, real in data:
        yosoku = a * hours + b  # その線での予測
        # 予測と実際のズレ（2乗してためる）
        e += (yosoku - real) ** 2
    return e


print("傾き5のときの誤差:", total_error(5, 35))
print("傾き7のときの誤差:", total_error(7, 35))
