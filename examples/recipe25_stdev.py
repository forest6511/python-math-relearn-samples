import statistics

class_a = [50, 50, 50, 50, 50]  # Aクラス：全員50点
class_b = [30, 40, 50, 60, 70]  # Bクラス：バラバラ

print("Aの平均 =", statistics.mean(class_a))
print("Bの平均 =", statistics.mean(class_b))
print("Aの標準偏差 =", statistics.pstdev(class_a))
print("Bの標準偏差 =", statistics.pstdev(class_b))
