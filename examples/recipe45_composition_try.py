import math


def nijou(x):
    return x**2


def nami(x):
    return math.sin(x)


for x in [0, 0.5, 1, 1.5, 2]:
    tochuu = nami(x)  # 先に波にする
    kekka = nijou(tochuu)  # その答えを二乗する
    print(
        f"x={x}: 波={round(tochuu, 3)}",
        f"→ 二乗={round(kekka, 3)}",
    )
