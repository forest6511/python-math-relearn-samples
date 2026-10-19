from scipy.stats import norm

heikin = 50  # 平均
sigma = 10  # ばらつき（標準偏差）

# 40点から60点まで（平均±10点）に入る割合
wariai = norm.cdf(60, heikin, sigma) - norm.cdf(
    40, heikin, sigma
)
print("40〜60点の割合:", round(wariai * 100, 1), "%")
