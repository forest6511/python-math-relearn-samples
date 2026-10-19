import numpy as np

# 0 から一周(2π)まで、4分の1周ずつ角度を進める
for kaiten in [0, 0.25, 0.5, 0.75, 1.0]:
    kaku = 2 * np.pi * kaiten  # 何周ぶんかを角度に直す
    # + 0.0 は、計算のごく小さな誤差で出る「-0.0」を
    # 0.0 にそろえるため
    print(
        f"{kaiten}周: sin =",
        round(np.sin(kaku), 2) + 0.0,
    )
