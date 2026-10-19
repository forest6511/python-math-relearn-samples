import math

for kazu in [5, 50, 500, 5000]:
    keta = round(math.log10(kazu), 2)
    print(f"{kazu} は 10 を 約{keta} 回かけた数")
