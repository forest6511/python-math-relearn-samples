import random
from collections import Counter

# 毎回おなじ結果が出るようにするおまじない
random.seed(0)

kekka = Counter()  # どの目が何回出たかを数える入れ物
for _ in range(10000):
    # 1から6のどれかをランダムに選ぶ
    me = random.randint(1, 6)
    kekka[me] += 1  # 出た目を1回ぶん数える

# 1から6まで、それぞれ何回出たかを表示する
for me in range(1, 7):
    print(me, "の目:", kekka[me], "回")
