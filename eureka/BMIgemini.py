import math

W = float(input())
H = float(input())
T = float(input())

H = H / 100
target_weight = T * (H ** 2)

diff = W - target_weight

if diff <= 0:
    print(0)
else:
    print(math.ceil(diff))


# BMI = 体重 / 身長**2
# 体重 = BMI * 身長**2
