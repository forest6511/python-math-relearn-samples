from sympy import expand, symbols

x = symbols("x")
left = (x + 1) ** 2
right = (
    x**2 + 2 * x + 2
)  # わざと最後を 2 にした（間違い）
print("同じ式か:", expand(left) == expand(right))
