"""レシピ27: 恒等式の検算。両辺を展開して同じ形になるか調べる。"""
from sympy import symbols, expand

x = symbols('x')
left = (x + 1)**2                # 左の式
right = x**2 + 2*x + 1           # 右の式
print("左を展開:", expand(left))
print("同じ式か:", expand(left) == expand(right))
