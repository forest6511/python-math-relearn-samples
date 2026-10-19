a, b, c = 1, -4, 1  # y = 1x^2 - 4x + 1 の a, b, c

vx = -b / (2 * a)  # 頂点の横の位置
# そのときの縦の位置（式に入れる）
vy = a * vx**2 + b * vx + c

print("頂点の x =", vx)
print("頂点の y =", vy)
