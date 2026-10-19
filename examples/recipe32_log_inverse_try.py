import math

kazu = 8
kaisuu = math.log2(kazu)  # 8 → 回数(3)
modotta = 2**kaisuu  # 回数(3) → 数に戻す
print("回数:", kaisuu, "→ 戻すと:", modotta)
