import numpy as np

for kaiten in [0, 0.25, 0.5, 0.75, 1.0]:
    kaku = 2 * np.pi * kaiten
    # sin の値を 2 倍する（振幅を変える）
    print(
        f"{kaiten}周: 2 × sin =",
        round(2 * np.sin(kaku), 2) + 0.0,
    )
