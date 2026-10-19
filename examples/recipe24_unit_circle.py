import math

# 0度から90度まで、点の (x, y) を出す
for kakudo in [0, 30, 60, 90]:
    rad = math.radians(kakudo)
    x = math.cos(rad)  # 横の位置 = コサイン
    y = math.sin(rad)  # 縦の位置 = サイン
    print(
        kakudo,
        "度 -> (x, y) = (",
        round(x, 3),
        ",",
        round(y, 3),
        ")",
    )
