import math
import statistics

class_b = [30, 40, 50, 60, 70]
heikin = statistics.mean(class_b)

# 手順1 平均からの差（偏差）
sa = [x - heikin for x in class_b]
# 手順2 差を2乗する
nijo = [d**2 for d in sa]
# 手順3 2乗を平均する（分散）
bunsan = statistics.mean(nijo)

print("偏差 =", sa)
print("2乗 =", nijo)
print("分散 =", bunsan)
print("pvariance =", statistics.pvariance(class_b))
# 手順4 √で元の単位（点）に戻す（標準偏差）
print("標準偏差 =", math.sqrt(bunsan))
print("pstdev =", statistics.pstdev(class_b))
