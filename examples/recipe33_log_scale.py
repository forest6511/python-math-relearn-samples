import math

for kazu in [10, 1000, 100000, 1000000]:
    # 10 を何回かけたら kazu になるか
    keta = math.log10(kazu)
    print(
        f"{kazu} は 10 を {keta} 回かけた数（桁の目安）"
    )
