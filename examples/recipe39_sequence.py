a = 3  # 最初の数（初項）
d = 2  # 毎回たす数（公差）

kou = a  # いまの数
for i in range(6):
    print(kou, end=" ")  # 横に並べて表示
    kou = kou + d  # 次は「いまの数 ＋ 2」
print()
