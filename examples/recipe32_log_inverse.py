import math

for kazu in [2, 8, 32, 1024]:
    # 2 を何回かけたら kazu になるか
    kaisuu = math.log2(kazu)
    print(f"{kazu} は 2 を {kaisuu} 回かけた数")
