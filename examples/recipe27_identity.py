from sympy import expand, symbols

x = symbols("x")  # x を文字として用意する

left = (x + 1) ** 2  # 左の式：(x + 1) の2乗
right = x**2 + 2 * x + 1  # 右の式：展開したと主張する式

# 左を展開した結果が、右とまったく同じか？
print("左を展開:", expand(left))
print("同じ式か:", expand(left) == expand(right))
