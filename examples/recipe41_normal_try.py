from scipy.stats import norm

heikin = 50
sigma = 10
# 30点から70点まで（平均±ばらつき2つ分）
wariai = norm.cdf(70, heikin, sigma) - norm.cdf(
    30, heikin, sigma
)
print("30〜70点の割合:", round(wariai * 100, 1), "%")
