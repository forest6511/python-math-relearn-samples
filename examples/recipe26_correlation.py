import statistics

hours = [1, 2, 3, 4, 5]  # 勉強時間
scores = [30, 50, 55, 70, 90]  # 点数

r = statistics.correlation(hours, scores)
print("相関係数 =", r)
