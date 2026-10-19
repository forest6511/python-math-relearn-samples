import random

# 乱数の出発点（種）を0に決める。
# 毎回おなじ結果になる
random.seed(0)

for kaisuu in [10, 100, 1000, 10000]:
    omote = 0  # 表が出た回数を数える
    for _ in range(kaisuu):
        # 1なら表、0なら裏とする
        if random.randint(0, 1) == 1:
            omote += 1
    wariai = omote / kaisuu  # 表が出た割合を計算する
    print(kaisuu, "回投げ -> 表の割合", wariai)
