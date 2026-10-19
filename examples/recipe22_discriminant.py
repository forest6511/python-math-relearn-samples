def discriminant(a, b, c):  # 判別式 D = b^2 - 4ac
    return b**2 - 4 * a * c


print("x^2 - x - 6  : D =", discriminant(1, -1, -6))
print("x^2 - 4x + 4 : D =", discriminant(1, -4, 4))
print("x^2 + x + 1  : D =", discriminant(1, 1, 1))
