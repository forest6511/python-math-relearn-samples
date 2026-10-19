def y(x):
    return x**2  # 放物線 y = x の2乗


for h in [1.0, 0.5, 0.1, 0.01, 0.001]:
    # x=1 と x=1+h の2点を結ぶ線の傾き
    katamuki = (y(1 + h) - y(1)) / h
    print(f"h = {h}: 傾き = {round(katamuki, 4)}")
