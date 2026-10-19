import statistics

hours = [1, 2, 3, 4, 5]
scores = [60, 40, 70, 30, 55]
r = statistics.correlation(hours, scores)
print("相関係数 =", r)
