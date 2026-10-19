import numpy as np

a = np.array([2, 0])  # 右向きの矢印（基準）

migi = np.array([2, 0])  # 同じ右向き
print("同じ向き:", np.dot(a, migi))

ue = np.array([0, 2])  # 上向き（直角）
print("直角:", np.dot(a, ue))

hidari = np.array([-2, 0])  # 左向き（逆向き）
print("逆向き:", np.dot(a, hidari))
