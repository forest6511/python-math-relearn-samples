# y = 2x + 3 のルール（傾き2、切片3）
def y(x):
    return 2 * x + 3


# x を 0,1,2,3,4 と入れて y を見る
for x in range(5):
    print(x, "->", y(x))
