# 勉強時間から、予測の点数を返す関数
def predict(hours, a, b):
    return a * hours + b


a = 8  # 傾き：1時間勉強すると、何点上がるか
b = 30  # 切片：まったく勉強しないときの点数

for hours in [0, 2, 4, 6]:
    print(
        f"勉強{hours}時間 → 予測{predict(hours, a, b)}点"
    )
