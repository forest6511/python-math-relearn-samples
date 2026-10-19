# 2つのサイコロの目の組を、全部数える
zenbu = 0  # 全部の組の数
nana = 0  # 和が7になる組の数
for a in range(1, 7):  # 1つ目のサイコロの目
    for b in range(1, 7):  # 2つ目のサイコロの目
        zenbu += 1
        if a + b == 7:
            nana += 1

print("全部の組:", zenbu)
print("和が7の組:", nana)
print("和が7になる確率:", nana, "/", zenbu)
