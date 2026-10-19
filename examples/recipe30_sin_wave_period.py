import numpy as np

# 8分の1周ずつ、半周まで見る
for kaiten in [0, 0.125, 0.25, 0.375, 0.5]:
    kaku = 2 * np.pi * kaiten
    # 角度のほうを 2 倍する（周期を変える）
    print(
        f"{kaiten}周: sin(2 × 角度) =",
        round(np.sin(2 * kaku), 2) + 0.0,
    )
