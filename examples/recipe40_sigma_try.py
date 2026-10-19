from sympy import summation, symbols

k, n = symbols("k n")  # k と n を文字として用意

# 1 から n まで k をたす（n のまま計算）
shiki = summation(k, (k, 1, n))
print("1からnまでの合計の式:", shiki)
print("n=10 を入れると:", shiki.subs(n, 10))
