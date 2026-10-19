zenin = 10  # 似た受験生の人数
goukaku = 7  # そのうち過去に合格した人数

jishin = goukaku / zenin
print(
    f"似た{zenin}人のうち{goukaku}人が合格 → "
    f"自信度 {jishin}（{int(jishin * 100)}%）"
)

# 合格した人数を変えると、自信度がどう変わるか
for goukaku in [0, 3, 5, 10]:
    print(
        f"合格{goukaku}人/{zenin}人 → "
        f"自信度 {goukaku / zenin}"
    )
