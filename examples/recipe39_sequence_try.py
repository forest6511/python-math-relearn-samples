a = 3  # 最初の数
r = 2  # 毎回かける数（公比）

kou = a
for i in range(6):
    print(kou, end=" ")
    kou = kou * r  # 次は「いまの数 × 2」
print()
