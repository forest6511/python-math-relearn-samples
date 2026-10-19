import numpy as np

# 質問を表す矢印（数にしたもの）
shitsumon = np.array([3, 1])
kotae_A = np.array([3, 1])  # 質問とそっくりな答え
kotae_B = np.array([-2, 1])  # 質問と方向がちがう答え

print(
    "質問と答えAの近さ（内積）:",
    np.dot(shitsumon, kotae_A),
)
print(
    "質問と答えBの近さ（内積）:",
    np.dot(shitsumon, kotae_B),
)
