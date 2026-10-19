import math

x1, y1 = 1, 2  # 点A の (横, 縦)
x2, y2 = 4, 6  # 点B の (横, 縦)

yoko = x2 - x1  # 横のズレ
tate = y2 - y1  # 縦のズレ

# 横のズレと縦のズレで、三平方の定理を使う
d = math.sqrt(yoko**2 + tate**2)
print("横のズレ =", yoko)
print("縦のズレ =", tate)
print("2点の距離 =", d)
