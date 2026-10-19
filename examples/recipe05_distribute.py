from sympy import expand, symbols

x = symbols("x")  # x を「文字」として用意する

# 2 * (x + 1) のかっこを外した形に直す
print(expand(2 * (x + 1)))
