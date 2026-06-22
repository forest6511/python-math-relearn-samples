"""レシピ33: 対数スケール。log10 はその数の桁の大きさを表す。"""
import math

for kazu in [10, 1000, 100000, 1000000]:
    keta = math.log10(kazu)
    print(f"{kazu} は 10 を {keta} 回かけた数（桁の目安）")
