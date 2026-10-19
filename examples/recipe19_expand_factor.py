from sympy import expand, factor, symbols

x = symbols("x")  # x を文字として用意する

# 展開: かっこを開く
print("展開:", expand((x + 2) * (x + 3)))

# 因数分解: かっこの形に戻す
print("因数分解:", factor(x**2 + 5 * x + 6))
