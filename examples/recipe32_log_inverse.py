"""レシピ32: 対数は指数の逆。2を何回かけたらその数になるか。"""
import math

for kazu in [2, 8, 32, 1024]:
    kaisuu = math.log2(kazu)
    print(f"{kazu} は 2 を {kaisuu} 回かけた数")
