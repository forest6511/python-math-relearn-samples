import math

a = 3  # 横の辺
b = 4  # 縦の辺

# a を2乗した数 と b を2乗した数 を足して、
# その平方根が斜辺
c = math.sqrt(a**2 + b**2)
print("斜辺の長さ =", c)
print("a^2 + b^2 =", a**2 + b**2)  # 9 + 16
print("c^2 =", c**2)  # 斜辺を2乗すると?
