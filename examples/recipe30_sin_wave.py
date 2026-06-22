"""レシピ30: 単位円の点の縦位置を並べると sin の波になる。"""
import numpy as np

for kaiten in [0, 0.25, 0.5, 0.75, 1.0]:
    kaku = 2 * np.pi * kaiten            # 何周ぶんかを角度に直す
    # + 0.0 は 0 が「-0.0」と表示されるのを直すおまじない
    print(f"{kaiten}周: sin =", round(np.sin(kaku), 2) + 0.0)
