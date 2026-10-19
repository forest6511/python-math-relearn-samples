# y = a × x のルール。x と、傾き a の2つを入れる機械
def y(x, a):
    return a * x


# 傾きを 1, 2, 3 と変えて、x=1 と x=2 のときの y を並べる
for a in [1, 2, 3]:
    print("傾き", a, "->", y(1, a), y(2, a))
