# レシピ8：平均と中央値 ＝ データの「真ん中」の出し方
import statistics

data = [40, 50, 60, 70, 80]
print("平均  :", statistics.mean(data))      # 平均を出す
print("中央値:", statistics.median(data))    # 中央値を出す

# 外れ値が混じると平均は引っぱられる
data = [40, 50, 60, 70, 1000]   # 1人だけ飛び抜けて高い
print("平均  :", statistics.mean(data))
print("中央値:", statistics.median(data))
