import numpy as np

# 0 から一周(2π)まで、4分の1周ずつ角度を進める
for kaiten in [0, 0.25, 0.5, 0.75, 1.0]:
    kaku = 2 * np.pi * kaiten  # 何周ぶんかを角度に直す
    # 最後の + 0.0 は、0が「-0.0」と表示されるのを
    # ただの0に直すおまじない
    print(
        f"{kaiten}周: sin =",
        round(np.sin(kaku), 2) + 0.0,
    )
