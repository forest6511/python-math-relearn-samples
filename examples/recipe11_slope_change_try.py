def y(x, a):
    return a * x


for a in [-1, -2, -3]:
    print("傾き", a, "->", y(1, a), y(2, a))
