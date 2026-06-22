"""レシピ13: 投げる回数を増やすと表の割合が0.5に近づく（大数の法則）。"""
import random

random.seed(0)  # 毎回おなじ結果が出るようにするおまじない

for kaisuu in [10, 100, 1000, 10000]:
    omote = 0                          # 表が出た回数を数える
    for _ in range(kaisuu):
        if random.randint(0, 1) == 1:  # 1なら表、0なら裏とする
            omote += 1
    wariai = omote / kaisuu            # 表が出た割合を計算する
    print(kaisuu, "回投げ -> 表の割合", wariai)
