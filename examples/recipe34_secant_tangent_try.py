def y(x):
    return x**2


for h in [1.0, 0.1, 0.01, 0.001]:
    katamuki = (y(3 + h) - y(3)) / h
    print(f"h = {h}: 傾き = {round(katamuki, 4)}")
