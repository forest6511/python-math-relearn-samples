import numpy as np

for kaiten in [0, 0.125, 0.25, 0.375, 0.5]:
    kaku = 2 * np.pi * kaiten
    print(f"{kaiten}周: sin =", round(np.sin(kaku), 2))
