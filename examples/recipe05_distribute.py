# レシピ5：かっこを外す（分配法則）と、同類項をまとめる
from sympy import symbols, expand, simplify

x = symbols('x')   # x を「文字」として用意する

# 2 * (x + 1) のかっこを外した形に直す
print(expand(2 * (x + 1)))        # -> 2*x + 2

# 同類項をまとめる
print(simplify(3 * x + 2 * x))        # -> 5*x
print(simplify(2 * x + 5 + 3 * x + 1))  # -> 5*x + 6
