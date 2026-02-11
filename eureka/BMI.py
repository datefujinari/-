import sys
# 標準入力からデータを読み込み、改行で分割
input_data = sys.stdin.read().split()

#体重と身長を取得
weight = int(input_data(0))
height = int(input_data(1))

#BMIを計算 BMI = 体重(kg) / 身(m)長 ** 2
BMI = weight / height ** 2

#BMIの目標値
target_BMI = int(input_data(2))

#BMIの目標値との差を計算
while BMI < target_BMI:
    count += 1

#BMIの目標値との差を出力
print(count) 