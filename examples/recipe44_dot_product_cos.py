import numpy as np


# 内積を、2本の矢印の長さでわる（cos θ が残る）
def muki(a, b):
    nagasa = np.linalg.norm(a) * np.linalg.norm(b)
    return round(np.dot(a, b) / nagasa, 3)


a = np.array([2, 0])  # 右向き
print("[2,0]と[2,0]:", np.dot(a, a), "→", muki(a, a))

c = np.array([2, 1])  # 右ななめ上
d = np.array([1, 3])  # 上ななめ右
print("[2,1]と[1,3]:", np.dot(c, d), "→", muki(c, d))
