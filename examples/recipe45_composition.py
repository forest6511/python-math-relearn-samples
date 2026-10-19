import math


def nijou(x):
    return x**2  # 二乗する機械


def nami(x):
    return math.sin(x)  # 波にする機械（sin）


for x in [0, 0.5, 1, 1.5, 2]:
    tochuu = nijou(x)  # まず二乗する
    kekka = nami(tochuu)  # その答えを波に入れる
    print(
        f"x={x}: 二乗={round(tochuu, 2)} "
        f"→ 波={round(kekka, 3)}"
    )
